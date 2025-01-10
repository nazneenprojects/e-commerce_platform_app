"""
order.py contains data model for db tables
"""
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.db import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    total_price = Column(Float, nullable=False)
    status = Column(String, nullable=False)


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_at_time = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)

    order = relationship("Order", backref="items")
    product = relationship("Product")

    @property
    def product_name(self) -> str:
        """Get the product name from the relationship"""
        return self.product.name if self.product else "Unknown Product"

    @property
    def unit_price(self) -> float:
        """Alias for price_at_time to match the schema"""
        return self.price_at_time
