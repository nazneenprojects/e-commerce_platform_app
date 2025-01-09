"""
this order.py contains schema details for order using pydantic validation
"""

from typing import List

from pydantic import BaseModel, Field


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)


class OrderCreate(BaseModel):
    items: List[OrderItemCreate]


class OrderItem(OrderItemCreate):
    price_at_time: float

    class Config:
        from_attributes = True


class Order(BaseModel):
    id: int
    items: List[OrderItem]
    total_price: float
    status: str

    class Config:
        from_attributes = True
