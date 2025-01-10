from unittest import mock
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.product import Product
from app.models.order import Order, OrderItem

client = TestClient(app)


@pytest.fixture
def mock_product():
    return Product(
        id=1,
        name="Test Product",
        description="Test Description",
        price=30.0,
        stock=10
    )


@pytest.fixture
def mock_db_session():
    session = mock.MagicMock()
    session.commit = mock.MagicMock()
    session.rollback = mock.MagicMock()
    session.refresh = mock.MagicMock()
    session.add = mock.MagicMock()
    session.bulk_save_objects = mock.MagicMock()
    session.flush = mock.MagicMock()

    # Mock refresh to update the mock_order id
    def mock_refresh(obj):
        if isinstance(obj, Order):
            obj.id = 1

    session.refresh.side_effect = mock_refresh

    return session


@pytest.fixture
def mock_product_service(mock_product, mock_db_session):
    # Mock product queries for all scenarios
    def query_side_effect(model):
        query = mock.MagicMock()

        # Mock filter().in_() for product lookup in order creation
        in_filter = mock.MagicMock()
        in_filter.all.return_value = [mock_product]
        query.filter.return_value.in_.return_value = in_filter

        # Mock direct filter() calls
        query.filter.return_value.all.return_value = [mock_product]
        query.filter.return_value.first.return_value = mock_product

        # Mock basic query operations
        query.all.return_value = [mock_product]
        query.get.return_value = mock_product

        return query

    mock_db_session.query.side_effect = query_side_effect
    return mock_db_session


@pytest.fixture(autouse=True)
def override_get_db(mock_db_session):
    with mock.patch("app.db.dependencies.get_db") as mock_get_db:
        def get_db():
            yield mock_db_session

        mock_get_db.return_value = get_db()
        yield


# def test_create_order_integration():
#     order_data = {
#         "products": [
#             {
#                 "product_id": 1,
#                 "quantity": 2
#             }
#         ]
#     }
#
#     response = client.post("/order/create_order", json=order_data)
#     assert response.status_code == 201
#
#     order = response.json()
#     assert "id" in order
#     assert order["total_price"] == 60.0  # 2 * 30.0
#     assert order["status"] == "completed"
#     assert isinstance(order["items"], list)
#     assert len(order["items"]) == 1
#
#     order_item = order["items"][0]
#     assert order_item["quantity"] == 2
#     assert order_item["price_at_time"] == 30.0  # Note: using price_at_time instead of unit_price
#     assert order_item["subtotal"] == 60.0
#     assert order_item["product_name"] == "Test Product"


def test_create_product_integration():
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 30.0,
        "stock": 10
    }

    response = client.post("/product/create_product", json=product_data)
    assert response.status_code == 200
    assert response.json()["name"] == product_data["name"]
    assert response.json()["price"] == product_data["price"]
    assert response.json()["stock"] == product_data["stock"]
    assert "id" in response.json()


def test_get_products_integration():
    response = client.get("/product/all_products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    product = response.json()[0]
    assert all(key in product for key in ["id", "name", "description", "price", "stock"])