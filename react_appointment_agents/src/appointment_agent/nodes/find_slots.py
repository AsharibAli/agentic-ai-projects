"""It includes a basic Tavily search function."""

from dotenv import find_dotenv, load_dotenv

from langchain_core.messages import ToolMessage

from appointment_agent.state import AppointmentAgentState
from appointment_agent.nodes._tools import schedule_tools_set

_: bool = load_dotenv(find_dotenv())

async def find_slots(state: AppointmentAgentState):
    """
    Determine if the conversation should continue to tools or end
    """
    messages = state["messages"]
    last_message = messages[-1]

    tool_messages = []

    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
      for call in last_message.tool_calls:
          tool_name = call.get("name")
          tool_id = call.get("id")
          args = call.get("args")

          find_free_slots_tool = next((tool for tool in schedule_tools_set if tool.name == tool_name), None)

          if tool_name == "GOOGLECALENDAR_FIND_FREE_SLOTS":
              res = find_free_slots_tool.invoke(args)
              tool_msg = ToolMessage(
                    name=tool_name,
                    tool_call_id=tool_id,
                    content=res,
                )
              tool_messages.append(tool_msg)
              
    return {"messages": tool_messages}
