from fastapi import FastAPI, HTTPException
from fastapi_mcp import FastApiMCP
from pydantic import BaseModel
from typing import Dict, Optional

# Define Item model
class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

app = FastAPI()

# Store items dictionary to simulate a database
store_items: Dict[int, Item] = {}

# Root endpoint that lists all available APIs
@app.get("/")
async def list_apis():
    """List all available APIs and their usage"""
    return {
        "available_apis": {
            "GET /items/": "Get all items in the store",
            "GET /items/{item_id}": "Get a specific item by ID",
            "POST /items/": "Create a new item. Required body: {name: string, price: float, description?: string}",
            "PUT /items/{item_id}": "Update an existing item. Required body: {name: string, price: float, description?: string}",
            "DELETE /items/{item_id}": "Delete an item by ID"
        }
    }

# GET - Get all items
@app.get("/items/")
async def get_items():
    """Get all items in the store"""
    return store_items

# GET - Get specific item by ID
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    """Get a specific item by ID"""
    if item_id not in store_items:
        raise HTTPException(status_code=404, detail="Item not found")
    return store_items[item_id]

# POST - Create new item
@app.post("/items/")
async def create_item(item: Item):
    """Create a new item"""
    # Generate new ID (simple increment)
    item_id = len(store_items) + 1
    store_items[item_id] = item
    return {"item_id": item_id, "item": item}

# PUT - Update existing item
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """Update an existing item"""
    if item_id not in store_items:
        raise HTTPException(status_code=404, detail="Item not found")
    store_items[item_id] = item
    return {"item_id": item_id, "item": item}

# DELETE - Delete an item
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Delete an item"""
    if item_id not in store_items:
        raise HTTPException(status_code=404, detail="Item not found")
    item = store_items.pop(item_id)
    return {"message": f"Item {item_id} deleted", "item": item}

mcp = FastApiMCP(
    app,
    # Optional parameters
    name="Store Items API",
    description="API for managing store items",
    base_url="http://localhost:8000",
)

# Mount the MCP server directly to your FastAPI app
mcp.mount()