from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["GEMINI_API_KEY"] = gemini_api_key

def openai():
    try:
        response = completion(
            model="openai/o3-mini",
            messages=[{"role": "user", "content": "Hello, how are you?"}],
        )
        
        print("\n" + "="*50)
        print(f"Content: {response.choices[0].message.content}")
        print(f"Model: {response.model}")
        print(f"Usage:")
        print(f"  Prompt Tokens: {response.usage.prompt_tokens}")
        print(f"  Completion Tokens: {response.usage.completion_tokens}")
        print(f"  Total Tokens: {response.usage.total_tokens}")
        print("="*50 + "\n")

    except Exception as e:
        print(f"Error occurred: {str(e)}")


def gemini():
    try:
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[{"role": "user", "content": "Hello, how are you?"}],
        )
        
        print("\n" + "="*50)
        print(f"Content: {response.choices[0].message.content}")
        print(f"Model: {response.model}")
        print(f"Usage:")
        print(f"  Prompt Tokens: {response.usage.prompt_tokens}")
        print(f"  Completion Tokens: {response.usage.completion_tokens}")
        print(f"  Total Tokens: {response.usage.total_tokens}")
        print("="*50 + "\n")
        

    except Exception as e:
        print(f"Error occurred: {str(e)}")
