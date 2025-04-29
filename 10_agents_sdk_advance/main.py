import asyncio
from agents import Agent, Runner
from agents.extensions.visualization import draw_graph
from agents import enable_verbose_stdout_logging

# Enable verbose logging
# enable_verbose_stdout_logging()

# Agent
webdev_agent = Agent(
    name="Web Development Agent",
    handoff_description="Specialist agent for web development-related questions",
    instructions="You are a helpful assistant that can answer questions about web development.",
    model="gpt-4.1-mini",
)

# Agent
mobiledev_agent = Agent(
    name="Mobile Development Agent",
    handoff_description="Specialist agent for mobile development-related questions",
    instructions="You are a helpful assistant that can answer questions about mobile development.",
    model="gpt-4.1-mini",
)

# Agent
devops_agent = Agent(
    name="DevOps Agent",
    handoff_description="Specialist agent for devops-related questions",
    instructions="You are a helpful assistant that can answer questions about devops.",
    model="gpt-4.1-mini",
)

# Agent
openai_agent = Agent(
    name="OpenAI Agent",
    handoff_description="Specialist agent for openai-related questions",
    instructions="You are a helpful assistant that can answer questions about openai.",
    model="gpt-4.1-mini",
)

# Agent as the Tool
devops_tool = devops_agent.as_tool(
    tool_name="devops_agent",
    tool_description="Specialist agent for devops-related questions",
)

# Agent as the Tool
openai_tool = openai_agent.as_tool(
    tool_name="openai_agent",
    tool_description="Specialist agent for openai-related questions",
)

# Lead Agent that uses the Tools
agenticai_agent = Agent(
    name="Agentic AI Agent",
    handoff_description="Specialist agent for agentic ai-related questions",
    instructions="You are a helpful assistant that can answer questions about agentic ai.",
    tools=[devops_tool, openai_tool],
    model="gpt-4.1-mini",
)

# Trainge Agent
trainge_agent = Agent(
    name="Trainge Agent",
    instructions="You determine which agent to use based on the user's question",
    handoffs=[
        webdev_agent,
        mobiledev_agent,
        agenticai_agent,
    ],
    model="gpt-4.1-mini",
)

# Draw the graph
# draw_graph(trainge_agent)


async def main():
    result = await Runner.run(trainge_agent, "What does a DevOps person do in Agentic AI?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
