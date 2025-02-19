# Explore MCP Server in Python

The Model Context Protocol (MCP) is a open protocol that lets you share data from (external systems like databases, APIs, etc.) to LLMs. Here's what MCP servers offer:

*   **Resources:** Share data with LLMs like `GET` endpoints in a web API.
*   **Tools:** Provide functions that LLMs can use like `POST` endpoints in a web API.
*   **Prompts:** Define reusable ways to interact with LLMs.
*   **And more!**: MCP offers other features to connect your AI applications to external systems.

## Installation

It's recommended to use `uv` to add mcp to your project.

```bash
uv init --package explore-mcp
uv add "mcp[cli]"
```

## Creating an MCP Server in `src/explore_mcp/server.py`

```python
# src/explore_mcp/server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

```

## Running the MCP Server

```bash
mcp dev src/explore_mcp/server.py
```

## Inspecting the MCP Server

```bash
mcp inspect src/explore_mcp/server.py
```
