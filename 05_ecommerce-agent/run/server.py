from fastapi import FastAPI
from routes.product_routes import router as product_router
import uvicorn
from config import Config

app = FastAPI(title="Asharib Shopping Mart API")

# Register routers
app.include_router(product_router)


def main():
    """Run the FastAPI server."""
    uvicorn.run("run.server:app", host="0.0.0.0", port=8080, reload=True)


if __name__ == "__main__":
    main()
