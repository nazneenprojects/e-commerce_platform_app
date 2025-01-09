"""
this product.py contains the product details validation using pydantic
"""
from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True