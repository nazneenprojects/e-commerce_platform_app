# e-commerce_platform_app
e-commerce_platform_app  with Tech Stack  Python3, FastAPI, PostgresSQL Docker, Unit testing, Render


## How to ?
1. To Run the project "poetry run uvicorn app.main:app --reload"
2. To install the poetry project : "poetry init"
3. To add the dependencies : "example, poetry add fastapi uvicorn"
4. To remove the poetry 
    "rm pyproject.toml poetry.lock"
    "poetry env remove python"
5. Alembic Set up:
    a. poetry add alembic
    b. alembic init alembic
    c. update files : env.py and alembic.ini
    d. before running app , generate migration script : alembic revision --autogenerate -m "Initial migration"
    e. apply migration:  alembic upgrade head


# E-Commerce Platform API

A production-grade RESTful API for an e-commerce platform built with FastAPI, PostgreSQL, and Docker.

## Features

- Product management (create, list)
- Order processing with stock validation
- Comprehensive error handling
- Database migrations with Alembic
- Structured logging
- Unit and integration tests
- Docker support

## Tech Stack

- Python 3.13+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Poetry
- Docker
- pytest

## Local Development Setup

1. Clone the repository:
```bash
git clone 
cd e-commerce_platform_app
```

2. Install dependencies with Poetry:
```bash
poetry install
```

3. Set up environment variables:
Create a `.env` file with:
```
DATABASE_URL=postgresql://user:password@localhost:5432/ecommerce_db
```

4. Run database migrations:
```bash
poetry run alembic upgrade head
```

5. Start the development server:
```bash
poetry run uvicorn app.main:app --reload
```

## Running Tests

Run unit tests:
```bash
poetry run pytest tests/unit/
```

Run integration tests:
```bash
poetry run pytest tests/integration/
```

## Docker Deployment

1. Build the Docker image:
```bash
docker build -t e-commerce-platform-app .
```

2. Run the container:
```bash
docker run -p 8000:8000 \
  -e DATABASE_URL=postgresql://user:password@host:5432/ecommerce_db \
  ecommerce-api
```

## API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Products
- `GET /product/all_products` - List all products
- `POST /product/create_product` - Create a new product

### Orders
- `POST /order/create_order` - Create a new order

## Error Handling

The API includes comprehensive error handling for:
- Insufficient stock
- Product not found
- Invalid order data
- Database errors

## Logging

Structured logging is implemented using `structlog`. Logs include:
- Request/response details
- Error information
- Business operations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request


