import pytest
from unittest.mock import Mock, patch, MagicMock
from sqlalchemy.orm import Session
from app.models.order import Order
from app.models.product import Product
from app.schemas.order import OrderCreate, OrderProductCreate
from app.service.order_service import OrderService
from app.utils.exceptions import StockException, ProductNotFoundException

@pytest.fixture
def db_session():
    return MagicMock(spec=Session)

def test_create_order_success(db_session):
    # Arrange
    order_data = OrderCreate(products=[
        OrderProductCreate(product_id=1, quantity=2)
    ])

    mock_product = Product(id=1, name="Test Product", price=10.0, stock=5)
    db_session.query.return_value.filter.return_value.all.return_value = [mock_product]

    # Act
    result = OrderService.create_order(db_session, order_data)

    # Assert
    assert isinstance(result, Order)
    assert result.total_price == 20.0  # 2 items * $10
    assert mock_product.stock == 3  # 5 initial - 2 ordered
    db_session.commit.assert_called_once()

def test_create_order_insufficient_stock(db_session):
    # Arrange
    order_data = OrderCreate(products=[
        OrderProductCreate(product_id=1, quantity=10)
    ])

    mock_product = Product(id=1, name="Test Product", price=10.0, stock=5)
    db_session.query.return_value.filter.return_value.all.return_value = [mock_product]

    # Act & Assert
    with pytest.raises(StockException):
        OrderService.create_order(db_session, order_data)
    db_session.rollback.assert_called_once()

def test_create_order_product_not_found(db_session):
    # Arrange
    order_data = OrderCreate(products=[
        OrderProductCreate(product_id=999, quantity=1)
    ])

    db_session.query.return_value.filter.return_value.all.return_value = []

    # Act & Assert
    with pytest.raises(ProductNotFoundException):
        OrderService.create_order(db_session, order_data)
    db_session.rollback.assert_called_once()
