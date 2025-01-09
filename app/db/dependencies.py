"""
products.py contains common db session dependency details
"""

from app.db.db import SessionLocal


# Dependency of Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()