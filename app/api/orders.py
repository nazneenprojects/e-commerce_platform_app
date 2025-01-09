"""
 order.py contains rest api endpoints related to orders
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.order import Order
from app.schemas.order import Order as OrderSchema
from app.schemas.order import OrderCreate

router = APIRouter(
    prefix="/order",
    tags=["Order Information"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not Found"}},
)

@router.post("/create_order", response_model=OrderSchema)
def create_order(
    order: OrderCreate,
    db_session: Session = Depends(get_db)):
    db_order = Order(total_price=0, status="pending")
    db_session.add(db_order)
    db_session.flush()

    total_price = 0

    #TODO : process_items logic here
    for item in order.items:
        pass

    return db_order
