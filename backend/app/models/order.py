from pydantic import BaseModel
from typing import List

class OrderItem(BaseModel):
    product_id: int
    quantity: int
    price: float

class Order(BaseModel):
    id: int
    customer_id: int
    seller_id: int
    items: List[OrderItem]
    status: str
    created_at: str
    updated_at: str
