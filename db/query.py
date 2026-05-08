from db.database import SessionLocal
from db.models import Book

"""
Database Query Module

Provides functionality to retrieve and display data from the database.
Used for testing and verifying that data has been correctly stored.
"""

def get_books():
    session = SessionLocal()

    books = session.query(Book).all()

    for book in books:
        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Sales: {book.sales}")

    session.close()

if __name__ == "__main__":
    get_books()