"""This module defines the react_tools for agent."""

from langgraph.prebuilt import ToolNode

from react_agent.tools import search, user_profile_finder

react_tools = [user_profile_finder, search]

react_tools_node = ToolNode(react_tools)
