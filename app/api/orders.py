"""
 order.py contains rest api endpoints related to orders
"""

from fastapi import APIRouter, Depends, HTTPException, status

from app.db.dependencies import get_db
from app.schemas.order import Order as OrderSchema
from app.schemas.order import OrderCreate
from app.service.order_service import OrderService
from app.utils.exceptions import ProductNotFoundException, StockException, OrderCreationException
from app.utils.logger import setup_logging, get_logger


#set up logging
setup_logging()
logger = get_logger(__name__)

router = APIRouter(
    prefix="/order",
    tags=["Order Information"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not Found"}},
)



@router.post("/create_order", response_model=OrderSchema, status_code=status.HTTP_201_CREATED)
def create_order(
        order_data: OrderCreate,
        db_session=Depends(get_db)
):
    """
    Create a new order with multiple products. To know product id please execute /products/all_products endpoint first

    Example request body:
    ```json
    {
        "products": [
            {
                "product_id": 1,
                "quantity": 2
            },
            {
                "product_id": 2,
                "quantity": 1
            }
        ]
    }
    ```
    """
    try:
        order = OrderService.create_order(db_session, order_data)
        logger.info(f"Order created in DB for {order_data.products}")
        return order
    except (ProductNotFoundException, StockException) as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except OrderCreationException as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )