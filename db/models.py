from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

"""
Database Models Module

Defines the database schema using SQLAlchemy ORM.
Contains table definitions that map Python objects to database tables.
"""

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    sales = Column(Float)