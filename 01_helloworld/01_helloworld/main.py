import os
from typing import Dict, Optional
from langchain_google_genai import ChatGoogleGenerativeAI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key with fallback to prevent None
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set")

# Initialize FastAPI app
app = FastAPI(
    title="Greeting API",
    description="API for generating contextual greetings using Gemini AI",
    version="1.0.0"
)

@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint that returns a Hello World message"""
    return {"message": "Hello World from Agentia AI!"}

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    # Initialize the LangChain generative AI model
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        max_retries=3,
        api_key=GEMINI_API_KEY,
        temperature=0.7
    )
except Exception as e:
    raise RuntimeError(f"Failed to initialize Gemini AI: {str(e)}")

class MessageRequest(BaseModel):
    """Request model for user messages"""
    message: str = Field(..., min_length=1, max_length=1000, description="User input message")

class MessageResponse(BaseModel):
    """Response model for API"""
    response: str
    error: Optional[str] = None

async def get_greeting_or_contextual_response(query: str) -> str:
    """
    Generate a response using the Gemini AI model.
    
    Args:
        query (str): User's input message
        
    Returns:
        str: Generated response
        
    Raises:
        Exception: If AI model fails to generate response
    """
    prompt = f"""
    You are a highly capable and friendly conversational assistant. Your task is to engage users with warm, concise, and helpful responses.

    If the user's input is a greeting (e.g., "Hello", "Hi", "Good morning"), respond with an enthusiastic and friendly greeting that makes them feel welcomed.

    If the input is not a greeting, politely explain that your current functionality is limited to handling greetings, and offer a cheerful remark to keep the interaction pleasant.

    Ensure all responses are professional, approachable, and aligned with a high-quality conversational assistant.

    User's Message: {query}
    """
    try:
        response = llm.invoke(prompt)
        return response.content.strip()
    except Exception as e:
        raise Exception(f"Failed to generate response: {str(e)}")

@app.post("/greeting", response_model=MessageResponse)
async def respond_to_message(request: MessageRequest) -> Dict[str, str]:
    """
    Process user message and generate a response.
    
    Args:
        request (MessageRequest): User message request
        
    Returns:
        Dict[str, str]: Response containing AI-generated message
        
    Raises:
        HTTPException: If message processing fails
    """
    try:
        response = await get_greeting_or_contextual_response(request.message)
        return MessageResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        log_level="info"
    )