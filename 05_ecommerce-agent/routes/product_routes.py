from fastapi import APIRouter, Body, HTTPException
from pydantic import BaseModel
from services.llm_service import LLMService
from models.database import Database
from typing import Dict, Any, Optional

router = APIRouter()


class ProductRequest(BaseModel):
    product_name: str
    product_details: str


class OrderResponse(BaseModel):
    status: str
    message: str
    order_details: Dict[str, Any]


@router.post("/llm", response_model=OrderResponse)
async def handle_llm(request: ProductRequest):
    product_name = request.product_name
    product_details = request.product_details

    slot = LLMService.classify_product(product_name, product_details)
    if slot is not None:
        Database.append_product(product_name, slot)

    return {
        "status": "success",
        "message": "Your product has been initiated for shipping.",
        "order_details": {
            "status": "processing",
            "processing ETA": "1-2 business days",
        },
    }
