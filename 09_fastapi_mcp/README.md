# A simple FastAPI app (Item Store) with MCP server

Install the dependencies:

```bash
uv add fastapi[standard] fastapi-mcp
```

To run the app, run the following command:

```bash
fastapi dev main.py
```

Add the following to your MCP Client as SSE URL:

```bash
http://localhost:8000/mcp
```

Use your MCP Client to play with the app like getting, adding, updating, deleting items.
