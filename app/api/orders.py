"""
 order.py contains rest api endpoints related to orders
"""

from fastapi import APIRouter, Depends

from app.db.dependencies import get_db
from app.models.order import Order
from app.schemas.order import Order as OrderSchema
from app.schemas.order import OrderCreate
from app.service.order_service import OrderService
from app.utils import logger

router = APIRouter(
    prefix="/order",
    tags=["Order Information"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not Found"}},
)

@router.post("/create_order", response_model=OrderSchema)
def create_order(
    order_data: OrderCreate,
    db_session=Depends(get_db)):
    #logger.info("creating_order")
    return OrderService.create_order(db_session, order_data)
