from unittest.mock import Mock
import pytest
from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate
from app.service.product_service import ProductService


@pytest.fixture
def db_session():
    return Mock(spec=Session)


def test_get_products_success(db_session):
    # Arrange
    mock_products = [
        Product(id=1, name="Product 1", description="Test", price=10.0, stock=100),
        Product(id=2, name="Product 2", description="Test", price=20.0, stock=200)
    ]
    db_session.query.return_value.offset.return_value.limit.return_value.all.return_value = mock_products

    # Act
    result = ProductService.get_products(db_session)

    # Assert
    assert len(result) == 2
    assert result[0].name == "Product 1"
    assert result[1].name == "Product 2"
    db_session.query.assert_called_once()


def test_create_product_success(db_session):
    # Arrange
    product_data = ProductCreate(
        name="Product 1",
        description="Description",
        price=15.0,
        stock=50
    )

    # Act
    result = ProductService.create_product(db_session, product_data)

    # Assert
    db_session.add.assert_called_once()
    db_session.commit.assert_called_once()
    db_session.refresh.assert_called_once()
