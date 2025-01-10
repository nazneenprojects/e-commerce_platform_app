"""
product_service.py contains any of the crud operation implementation
"""
from typing import List

from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate
from app.utils.logger import get_logger, setup_logging

#set up logging
setup_logging()
logger = get_logger(__name__)

class ProductService:

    @staticmethod
    def get_products(db_session: Session, skip: int = 0, limit: int = 100) -> List[Product]:
        logger.info("fetching all products from DB")
        return db_session.query(Product).offset(skip).limit(limit).all()


    @staticmethod
    def create_product(db_session: Session, product_data: ProductCreate) -> Product:
        try:
            # Creating a new product object
            db_product = Product(
                name=product_data.name,
                description=product_data.description,
                price=product_data.price,
                stock=product_data.stock
            )

            # Add the product to the session
            db_session.add(db_product)
            logger.info("Added new product into DB")

            # Commit the transaction
            db_session.commit()

            # Refresh the product to get the latest state from the DB
            db_session.refresh(db_product)
            logger.info(f"Product {db_product.id} created successfully with name {db_product.name}")

            return db_product

        except IntegrityError as e:
            db_session.rollback()
            logger.error(f"Integrity error while creating product: {str(e)}")
            raise Exception("Product creation failed due to integrity constraints.")

        except SQLAlchemyError as e:
            db_session.rollback()
            logger.error(f"Database error while creating product: {str(e)}")
            raise Exception("Product creation failed due to a database error.")

        except Exception as e:
            db_session.rollback()
            logger.error(f"Unexpected error while creating product: {str(e)}")
            raise Exception("An unexpected error occurred while creating the product.")
