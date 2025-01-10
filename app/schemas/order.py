"""
this order.py contains schema details for order using pydantic validation
"""

from typing import List

from pydantic import BaseModel, Field, conlist


class OrderProductCreate(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., gt=0)


class OrderCreate(BaseModel):
    products: conlist(OrderProductCreate, min_length=1)



class OrderItemResponse(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    unit_price: float
    subtotal: float

    class Config:
        from_attributes = True
        alias_generator = lambda x: "price_at_time" if x == "unit_price" else x


class Order(BaseModel):
    id: int
    items: List[OrderItemResponse]
    total_price: float
    status: str

    class Config:
        from_attributes = True