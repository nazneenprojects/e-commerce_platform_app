"""
order_service.py contains required crud operation implementation
"""


from sqlalchemy.orm import Session
from typing import List, Tuple

from app.models.product import Product
from app.models.order import Order, OrderItem
from app.schemas.order import OrderCreate
from app.utils.exceptions import StockException, ProductNotFoundException, OrderCreationException
from app.utils.logger import setup_logging, get_logger

#set up logging
setup_logging()
logger = get_logger(__name__)

class OrderService:
    @staticmethod
    def validate_products_stock(
            db_session: Session,
            products_to_order: List[Tuple[int, int, Product]]
    ) -> None:
        """Validate stock availability for all products in the order."""
        logger.info("validating stock availability for the product stock")
        for product_id, quantity, product in products_to_order:
            if not product:
                logger.error("product not found")
                raise ProductNotFoundException( product_id=product_id, product_name="Unknown Product")
            if product.stock < quantity:
                logger.error("stock insufficient")
                raise StockException(
                    product_id=product_id,
                    product_name=product.name
                )

    @staticmethod
    def update_product_stock(
            db_session: Session,
            products_to_update: List[Tuple[int, int, Product]]
    ) -> None:
        """Update stock levels for all products in the order."""
        for _, quantity, product in products_to_update:
            product.stock -= quantity
            logger.info("updating stock quantity")
            db_session.add(product)

    @staticmethod
    def create_order_items(
            db_session: Session,
            order_id: int,
            products_to_process: List[Tuple[int, int, Product]]
    ) -> Tuple[List[OrderItem], float]:
        """Create order items and calculate total price."""
        order_items = []
        total_price = 0

        for product_id, quantity, product in products_to_process:
            subtotal = product.price * quantity
            order_item = OrderItem(
                order_id=order_id,
                product_id=product.id,
                quantity=quantity,
                price_at_time=product.price,  # This will be mapped to unit_price in response
                subtotal=subtotal
            )
            logger.debug("calculated price based on order items for {order_item}")
            order_items.append(order_item)
            total_price += subtotal

        return order_items, total_price

    @staticmethod
    def create_order(db_session: Session, order_data: OrderCreate) -> Order:
        try:
            # Fetch all products and validate in a single query
            product_ids = [item.product_id for item in order_data.products]
            logger.debug(f"creating order based on given order data for : {product_ids}")
            products = {
                p.id: p for p in
                db_session.query(Product).filter(Product.id.in_(product_ids)).all()
            }

            # Prepare products data for validation
            products_to_process = [
                (item.product_id, item.quantity, products.get(item.product_id))
                for item in order_data.products
            ]

            # Validate stock availability
            OrderService.validate_products_stock(db_session, products_to_process)

            # Create order
            db_order = Order(total_price=0, status="pending")
            db_session.add(db_order)
            db_session.flush()  # Get order ID

            # Create order items and calculate total
            order_items, total_price = OrderService.create_order_items(
                db_session, db_order.id, products_to_process
            )

            # Add all order items
            db_session.bulk_save_objects(order_items)

            # Update product stock levels
            OrderService.update_product_stock(db_session, products_to_process)

            # Update order total and status
            db_order.total_price = total_price
            db_order.status = "completed"

            # Commit all changes
            db_session.commit()

            # Refresh to ensure relationships are loaded
            db_session.refresh(db_order)
            logger.info("completed order creation")
            return db_order

        except (ProductNotFoundException, StockException) as e:
            logger.info("about to perform rollback due to exception")
            db_session.rollback()
            logger.error("exception occurred")
            raise
        except Exception as e:
            logger.info("about to perform rollback due to exception")
            db_session.rollback()
            logger.error("exception occurred")
            raise OrderCreationException(f"Failed to create order: {str(e)}")