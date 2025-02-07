"""This module defines the tools for agent."""

import os
import dotenv
import logging

from langgraph.prebuilt import ToolNode
from composio_langgraph import Action, ComposioToolSet
from appointment_agent.tools.make_confirmation_call import make_confirmation_call

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
)
logger = logging.getLogger(__name__)

# Load environment variables
dotenv.load_dotenv()

# Initialize ComposioToolSet with API key from environment variables
composio_toolset = ComposioToolSet(api_key=os.getenv("COMPOSIO_API_KEY"))

# Get the required tools
schedule_tools_set = composio_toolset.get_tools(
    actions=[
        Action.GOOGLECALENDAR_FIND_FREE_SLOTS,
        Action.GOOGLECALENDAR_CREATE_EVENT,
        Action.GMAIL_CREATE_EMAIL_DRAFT
    ]
)

# Separate out 
schedule_tools_write = composio_toolset.get_tools(
    actions=[
        Action.GOOGLECALENDAR_CREATE_EVENT,
        Action.GMAIL_CREATE_EMAIL_DRAFT
    ]
)

schedule_tools_write_node = ToolNode(schedule_tools_write + [make_confirmation_call])