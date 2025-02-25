from groq import Groq
from config import Config

client = Groq(api_key=Config.GROQ_API_KEY)

class LLMService:
    @staticmethod
    def classify_product(product_name, product_details):
        prompt = f"""
        Classify the following product into a shipping slot based on its price:
        Product: {product_name}
        Price: ${product_details}

        Shipping slots:
        Slot 1: Price <= $25
        Slot 2: $25 < Price <= $50
        Slot 3: $50 < Price <= $75
        Slot 4: $75 < Price <= $100
        Slot 5: Price > $100

        Respond with only the slot number (1, 2, 3, 4, or 5).
        """

        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": """
                You are a helpful assistant designed to classify comments into: 
                Neutral, Request, Question, Appreciation, Error or Other. 
                Must respond with one word.
                """},
                {"role": "user", "content": "Smart TV: $599.99"},
                {"role": "assistant", "content": "5"},
                {"role": "user", "content": "USB Flash Drive: $19.99"},
                {"role": "assistant", "content": "1"},
                {"role": "user", "content": "Portable Fan: $24.99"},
                {"role": "assistant", "content": "1"},
                {"role": "user", "content": "Microphone: $79.99"},
                {"role": "assistant", "content": "4"},
                {"role": "user", "content": "Laptop Charger: $39.99"},
                {"role": "assistant", "content": "2"},
                {"role": "user", "content": prompt}
            ]
        )

        try:
            slot = int(response.choices[0].message.content.strip())
            if 1 <= slot <= 5:
                return slot
            else:
                raise ValueError
        except ValueError:
            print(f"Invalid LLM response: {response.choices[0].message.content}")
            return None