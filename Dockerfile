# Use Python 3.13 slim base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*


# Install Poetry globally
RUN pip install poetry

# Debug: Verify Poetry installation
RUN poetry --version

# Copy project files
COPY pyproject.toml poetry.lock ./
COPY README.md ./
COPY app/ ./app/
COPY alembic.ini ./
COPY alembic/ ./alembic/

# Install dependencies
# Install dependencies without project installation
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction \
    && rm -rf /root/.cache/pypoetry

# Set environment variables
ENV PYTHONPATH=/app
ENV PORT=8000

# Expose port
EXPOSE 8000

# Run migrations and start the application
CMD ["sh", "-c", "alembic upgrade head && poetry run uvicorn app.main:app --host 0.0.0.0 --port $PORT"]
