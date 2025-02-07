import requests
import dotenv
import os

# Load environment variables
dotenv.load_dotenv()

BLAND_API_KEY = os.environ.get("BLAND_API_KEY")
def make_confirmation_call(phone_number: str, instructions: str):
    """
    Makes a confirmation call using the Bland.ai API.
    
    Parameters:
        phone_number (str): The recipient's phone number.
        instructions (str): The message to be delivered.
        api_key (str): The API authorization key.
    
    Returns:
        dict: The API response as a dictionary.
    """
    url = "https://api.bland.ai/v1/calls"

    payload = {
        "phone_number": phone_number,
        "task": instructions
    }
    
    headers = {
        "authorization": BLAND_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    return response.json()  # Returns the response as a dictionary