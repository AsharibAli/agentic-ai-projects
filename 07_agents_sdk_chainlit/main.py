import os
import chainlit as cl
from agents import Agent, Runner, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv
from agents.tool import function_tool

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Step 1: Provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# Step 2: Model

model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)

# Step 3: Config
config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True,
)


@function_tool("get_weather")
def get_weather(location: str, unit: str = "C") -> str:
    """
    Fetch the weather for a given location, returning a short description.
    """
    # Example logic
    return f"The weather in {location} is 22 degrees {unit}."


@function_tool("piaic_student_finder")
def student_finder(student_roll: int) -> str:
    """
    find the PIAIC student based on the roll number
    """
    data = {1: "Qasim", 2: "Sir Zia", 3: "Daniyal"}

    return data.get(student_roll, "Not Found")


# Step 4: Agent
agent = Agent(
    instructions="You are a helpful assistant that can answer questions and help with tasks.",
    name="Support Agent",
    tools=[get_weather, student_finder],  # add tools here
    model=model,
)


@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello, how can I help you today?").send()


@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")

    msg = cl.Message(content="")
    await msg.send()

    history.append({"role": "user", "content": message.content})
    result = Runner.run_streamed(
        agent,
        input=history,
        run_config=config,
    )
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(
            event.data, ResponseTextDeltaEvent
        ):
            await msg.stream_token(event.data.delta)
    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)
    # await cl.Message(content=result.final_output).send()
