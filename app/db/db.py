"""
db.py contains database connection details
"""
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.utils.logger import setup_logging, get_logger

#set up logging
setup_logging()
logger = get_logger(__name__)

load_dotenv()

db_url = os.getenv("DATABASE_URL")

# Construct connection string
SQLALCHEMY_DATABASE_URL = db_url

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session local class for handling database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# Create a base class for models
Base = declarative_base()


# def get_db():
#     logger.info("created db session")
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         logger.info("closing db session")
#         db.close()
