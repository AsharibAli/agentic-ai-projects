"""Searches for profile info based on user id from config."""

from typing import Annotated, Any, Dict, Optional, Union

from langchain_core.runnables import RunnableConfig
from langchain_core.tools import InjectedToolArg, tool


@tool(parse_docstring=False)
def user_profile_finder(
    config: Annotated[RunnableConfig, InjectedToolArg],
) -> Dict[str, Union[bool, Dict[str, Any], str, None]]:
    """Search for user info based on user id from config."""
    try:
        # Extract user location from config
        user_id: Optional[Dict[str, float | str]] = config.get("configurable", {}).get(
            "user_id"
        )
        return {
            "success": True,
            "data": None,
            "user_id": user_id,
        }

    except Exception as error:
        return {"success": False, "error": str(error), "search_location": None}
