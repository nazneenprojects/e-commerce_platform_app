"""
products.py contains rest api endpoints related to products
"""
from fastapi import APIRouter, Depends, HTTPException
from app.db.dependencies import get_db
from app.schemas.product import ProductCreate, Product as ProductSchema
from app.service import product_service


router = APIRouter(
    prefix="/product",
    tags=["Product Information"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not Found"}},
)


@router.get("/all_products", response_model=list[ProductSchema])
def get_products(db_session=Depends(get_db)):
    product_list = product_service.get_all_products(db_session)

@router.post("/create_product", response_model=ProductSchema)
def add_product(product: ProductCreate, db_session=Depends(get_db)):
    product_added = product_service.create_product(db_session)


