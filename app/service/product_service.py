"""
product_service.py contains any of the crud operation implementation
"""
from sqlalchemy.orm import Session
from app.models import product
from app.models.product import Product

def get_all_products(db_session: Session):
    return db_session.query(product).all()

def create_product(db_session: Session):
    db_product = Product(**product.dict())
    db_session.add(db_product)
    db_session.commit()
    db_session.refresh(db_product)
    return db_product