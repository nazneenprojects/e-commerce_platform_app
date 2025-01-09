"""
product_service.py contains any of the crud operation implementation
"""
from typing import List

from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate


class ProductService:

    @staticmethod
    def get_products(db: Session, skip: int = 0, limit: int = 100) -> List[Product]:
        return db.query(Product).offset(skip).limit(limit).all()


    @staticmethod
    def create_product(db: Session, product_data: ProductCreate) -> Product:
        db_product = Product(
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            stock=product_data.stock
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
