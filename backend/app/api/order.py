from fastapi import APIRouter, Depends
from typing import List
from ..models.order import Order

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=Order)
async def create_order(order: Order):
    # placeholder implementation
    return order

@router.get("/", response_model=List[Order])
async def list_orders():
    # placeholder implementation
    return []
