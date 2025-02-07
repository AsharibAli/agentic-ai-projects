from crewai.flow.flow import Flow, start, listen
from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = os.getenv("MODEL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class MainFlow(Flow):
    model = MODEL

    @start()
    def list_billionares(self):
        response = completion(
            model=self.model,
            api_key=GEMINI_API_KEY,
            messages=[{
                "role": "user",
                "content": "List the top 10 richest billionaires with their rankings."
            }]
        )
        list = response["choices"][0]["message"]["content"].strip()
        print(f"Top 10 Billionaires: {list} ")
        return list

    @listen(list_billionares)
    def wealth_source(self, list):
        response = completion(
            model=self.model,
            messages=[{
                "role": "user",
                "content": f"For each billionaire in '{list}', provide their primary source of wealth."
            }]
        )
        source = response["choices"][0]["message"]["content"].strip()
        print("Primary sources of wealth: ")
        print(source)
        return source

    @listen(wealth_source)
    def golden_advice(self, source):
        response = completion(
            model=self.model,
            messages=[{
                "role": "user",
                "content": f"Based on the wealth sources '{source}', provide one key piece of actionable advice from these billionaires."
            }]
        )
        advice = response["choices"][0]["message"]["content"].strip()
        print("Key actionable advice: ")
        print(advice)
        return advice
    
def main() -> None:
    flow = MainFlow()
    answer = flow.kickoff()
    print("Final Answer: ")
    print(answer)