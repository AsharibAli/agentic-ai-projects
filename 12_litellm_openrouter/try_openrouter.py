import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def main():
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    if not api_key:
        print("Error: OPENROUTER_API_KEY not found!")
        return

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    user_input = input("Enter your message: ")

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        max_tokens=100,
    )

    print("OpenRouter Response:")
    print("=" * 40)
    print(response.choices[0].message.content)
    print("=" * 40)
    print(f"Model used: {response.model}")


if __name__ == "__main__":
    main()
