# E-Commerce Platform API

A production-grade RESTful API for an e-commerce platform built with FastAPI, PostgreSQL, and Docker.
Live Render hosting URL - https://e-commerce-platform-app-latest.onrender.com/docs
![api.png](api.png)

## Features

- Product management (create, list)
- Order processing with stock validation
- Comprehensive error handling
- Cloud based Postgres Database hosting over Render (https://render.com/)
- Database migrations with Alembic
- Structured logging
- Unit and integration tests
- Docker support
- Live Render Hosting (available live for limited period)
- API Specification and Schema :
Swagger http://127.0.0.1:8000/docs#/
Redoc http://127.0.0.1:8000/redoc

## Tech Stack

- Python 3.13+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Poetry
- Docker
- pytest

## Approach :
# E-commerce Platform API

This FastAPI-based e-commerce platform demonstrates production-grade practices through a thoughtfully designed order 
management system. The application uses a junction table (OrderItem) approach for handling order-product relationships, 
enabling efficient tracking of pricing, maintaining order integrity, and supporting complex queries. 
The data model leverages SQLAlchemy with PostgreSQL, implementing proper foreign key constraints and relationships 
between Products, Orders, and OrderItems tables.

The application architecture follows best practices with clear separation of concerns: models for database schema, 
Pydantic schemas for validation, services for business logic, and controllers for API endpoints. 
Error handling is implemented through custom exception classes and proper HTTP status codes. 
The codebase is production-ready with features like input validation, stock management, transactional integrity, and 
comprehensive logging. The application is containerized using Docker for consistent deployment, with separate 
configurations for development and production environments.

The system includes thorough testing coverage with unit tests for business logic and integration tests for API endpoints
using pytest. Database migrations are handled through Alembic, ensuring smooth schema updates. The application is 
configured for deployment on Render with PostgreSQL database integration, demonstrating real-world deployment practices. 
Documentation is automatically generated through FastAPI's built-in Swagger UI, making API exploration 
and testing straightforward.


### Database Design with Junction Table:
Main tables: Products, Orders, OrderItems (junction table)
Benefits of junction table (OrderItems) approach:

Maintains historical pricing with price_at_time
Enables many-to-many relationship between Orders and Products
Stores quantity and subtotal per item
Preserves order data even if products change/delete
Easier reporting and analytics

### Modular structure:
Models (SQLAlchemy)
Schemas (Pydantic)
Services (Business logic)
Routes (API endpoints)

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
 docker run -d -p 8080:8000 -e DATABASE_URL=postgresql://********************-a.frankfurt-postgres.render.com/ecomdb_0l2p 
 --name e-commerce-app-container e-commerce-platform-app:latest


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
- Invalid order creation
- Database errors

## Logging

Structured logging is implemented using `structlog`. Logs include:
- Error information
- Business operations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## Render Deployment
This backend service is available via Render platform where docker container is running from docker registry
Render is a cloud platform designed for deploying and hosting applications and services. It simplifies the 
process of building, deploying, and managing apps by abstracting much of the infrastructure management, 
allowing developers to focus on their application code.

this backend service is hosted on render -   https://e-commerce-platform-app-latest.onrender.com/docs

## Future Scope
- Authentication using OAuth
- CI/CD deployment
- scaling using K8s
- performance monitoring using Grafana or Datadog or Dynatrace
- Rate limiting
- UUID support
- https security

