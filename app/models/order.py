"""
order.py contains data model for db tables
"""
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.db import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    # products = Column(JSON)
    total_price = Column(Float)
    status = Column(String)


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    price_at_time = Column(Float)

    order = relationship("Order", backref="items")
    product = relationship("Product")
