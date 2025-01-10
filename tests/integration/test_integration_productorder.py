# from fastapi.testclient import TestClient
# import pytest
# from app.main import app
# from app.db.dependencies import get_db
#
# client = TestClient(app)
#
#
# # Mock database session for integration tests
# @pytest.fixture
# def test_db():
#     db = next(get_db())
#     try:
#         yield db
#     finally:
#         db.rollback()
#         db.close()
#
#
# def test_create_product_integration():
#     product_data = {
#         "name": "Integration Test Product",
#         "description": "Test Description",
#         "price": 25.0,
#         "stock": 100
#     }
#
#     response = client.post("/product/create_product", json=product_data)
#     assert response.status_code == 200
#     assert response.json()["name"] == product_data["name"]
#     assert response.json()["price"] == product_data["price"]
#
#
# def test_get_products_integration():
#     response = client.get("/product/all_products")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)
#
#
# def test_create_order_integration():
#     # First create a product to order
#     product_data = {
#         "name": "Product for Order",
#         "description": "Test Description",
#         "price": 30.0,
#         "stock": 10
#     }
#     product_response = client.post("/product/create_product", json=product_data)
#     product_id = product_response.json()["id"]
#
#     # Create order
#     order_data = {
#         "products": [
#             {
#                 "product_id": product_id,
#                 "quantity": 2
#             }
#         ]
#     }
#
#     response = client.post("/order/create_order", json=order_data)
#     assert response.status_code == 201
#     assert response.json()["total_price"] == 60.0
#     assert response.json()["status"] == "completed"
