import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base

"""
Database Configuration Module

Sets up the database connection and session management using SQLAlchemy.
Responsible for creating the engine, session factory, and initializing tables.
"""

load_dotenv()

# SQLite database (file will be created automatically)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./books.db")

engine = create_engine(DATABASE_URL, echo = False)

SessionLocal = sessionmaker(bind=engine)

# Create tables based on the models
Base.metadata.create_all(bind=engine)