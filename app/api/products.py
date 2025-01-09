"""
products.py contains rest api endpoints related to products
"""
from fastapi import APIRouter, Depends

from app.db.dependencies import get_db
from app.schemas.product import ProductCreate, Product as ProductSchema
from app.service.product_service import ProductService

router = APIRouter(
    prefix="/product",
    tags=["Product Information"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not Found"}},
)


@router.get("/all_products", response_model=list[ProductSchema])
def get_products(skip: int = 0,
                 limit: int = 100,
                 db_session=Depends(get_db)):
    return ProductService.get_products(db_session, skip=skip, limit=limit)


@router.post("/create_product", response_model=ProductSchema)
def add_product(product_data: ProductCreate, db_session=Depends(get_db)):
    return ProductService.create_product(db_session, product_data)
