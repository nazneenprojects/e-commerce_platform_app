from fastapi import HTTPException

class StockException(HTTPException):
    def __init__(self, product_id: int):
        super().__init__(
            status_code=400,
            detail=f"Insufficient stock for product {product_id}"
        )

class ProductNotFoundException(HTTPException):
    def __init__(self, product_id: int):
        super().__init__(
            status_code=404,
            detail=f"Product {product_id} not found"
        )

class OrderCreationException(HTTPException):
    def __init__(self, detail: str = "Order creation failed"):
        super().__init__(
            status_code=400,
            detail=detail
        )