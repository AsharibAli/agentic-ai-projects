# Import necessary classes from agents module and asyncio for async operations
from agents import Agent, Runner
import asyncio

# Create an agent specialized in Pakistan-related questions
pakistan_agent = Agent(
    name="Pakistan Agent",
    instructions="You are a helpful assistant that can answer questions about Pakistan.",
)

# Create an agent specialized in historical topics
history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",  # Description used when referring to this agent
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
)

# Create an agent specialized in mathematical problems
math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for mathematical questions",  # Description used when referring to this agent
    instructions="You provide assistance with mathematical queries. Explain the concepts and steps clearly.",
)

# Create a triage agent that will direct questions to the appropriate specialist agent
trainge_agent = Agent(
    name="Trainge Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[
        history_tutor_agent,
        math_tutor_agent,
        pakistan_agent,
    ],  # List of specialist agents this agent can refer to
)


# Define the main async function that will run our agent
async def main():
    # Run the triage agent with a specific question and await its response
    result = await Runner.run(trainge_agent, "Who started the Pakistan Movement?")
    # Print the final response from the agent
    print(result.final_output)


# Standard Python idiom to run the main function only if this file is run directly
if __name__ == "__main__":
    # Run the async main function using asyncio
    asyncio.run(main())
