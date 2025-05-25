import json
from typing import cast
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import datetime, UTC
from uuid import uuid4
from agents import (
    Agent,
    Runner,
    function_tool,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    RunConfig,
    ModelProvider,
)
from fastapi.responses import StreamingResponse
from openai.types.responses import ResponseTextDeltaEvent

from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=cast(ModelProvider, external_client),  # satisfy type checker
    tracing_disabled=True,
)

app = FastAPI(
    title="Chatbot API with OpenAI Agents SDK",
    description="A FastAPI based API for a chatbot using OpenAI Agents SDK",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Metadata(BaseModel):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))
    session_id: str = Field(default_factory=lambda: str(uuid4()))


class Message(BaseModel):
    user_id: str
    text: str
    metadata: Metadata | None = None
    tags: list[str] | None = None


class Response(BaseModel):
    user_id: str
    reply: str
    metadata: Metadata


@function_tool
def get_current_time() -> str:
    """Returns the current time in UTC"""
    return datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC")


chat_agent = Agent(
    name="ChatAgent",
    instructions="You are a helpful chatbot. Respond to user messages in a friendly and informative way. If the user asks for the time, use the get_current_time tool.",
    model=model,
    tools=[get_current_time],
)


# Root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Get user endpoint
@app.get("/users/{user_id}")
async def get_user(user_id: str, role: str | None = None):
    user_info = {"user_id": user_id, "role": role if role else "guest"}
    return user_info


# Chat endpoint
@app.post("/chat/", response_model=Response)
async def chat(message: Message):
    if not message.text.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    result = await Runner.run(chat_agent, input=message.text)
    reply_text = result.final_output

    return Response(user_id=message.user_id, reply=reply_text, metadata=Metadata())


async def stream_response(message: Message):
    result = Runner.run_streamed(chat_agent, input=message.text, run_config=config)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(
            event.data, ResponseTextDeltaEvent
        ):
            print(event.data.delta, end="", flush=True)
            chunk = json.dumps({"chunk": event.data.delta})
            yield f"data: {chunk}\n\n"


@app.post("/chat/stream", response_model=Response)
async def chat_stream(message: Message):
    if not message.text.strip():
        raise HTTPException(status_code=400, detail="Message text cannot be empty")

    return StreamingResponse(stream_response(message), media_type="text/event-stream")
