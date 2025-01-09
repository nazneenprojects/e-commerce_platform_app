"""
order_service.py contains any of the crud operation implementation
"""

from sqlalchemy.orm import Session
from app.models.product import Product
from app.models.order import Order, OrderItem
from app.schemas.order import OrderCreate
from app.utils import logger
from app.utils.exceptions import StockException, ProductNotFoundException, OrderCreationException



class OrderService:

    @staticmethod
    def create_order(db: Session, order_data: OrderCreate) -> Order:
        #logger.info("creating_order")

        try:
            # Create order
            db_order = Order(total_price=0, status="pending")
            db.add(db_order)
            db.flush()

            total_price = 0

            # Process items
            for item in order_data.items:
                product = db.query(Product).filter(Product.id == item.product_id).first()
                if not product:
                    raise ProductNotFoundException(item.product_id)

                if product.stock < item.quantity:
                    raise StockException(item.product_id)

                # Create order item
                order_item = OrderItem(
                    order_id=db_order.id,
                    product_id=product.id,
                    quantity=item.quantity,
                    price_at_time=product.price
                )
                db.add(order_item)

                # Update stock and total
                product.stock -= item.quantity
                total_price += product.price * item.quantity

            db_order.total_price = total_price
            db.commit()

            #logger.info("order_created_successfully", order_id=db_order.id)
            return db_order

        except (ProductNotFoundException, StockException) as e:
            db.rollback()
            #logger.error("order_creation_failed", error=str(e.detail))
            raise
        except Exception as e:
            db.rollback()
            #logger.error("order_creation_failed", error=str(e))
            raise OrderCreationException()