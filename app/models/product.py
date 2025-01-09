"""
product.py contains data model for product table
"""

from sqlalchemy import Column, Integer, String, Float

from app.db.db import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)
