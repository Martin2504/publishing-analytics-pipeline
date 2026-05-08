from fastapi import FastAPI
from db.database import SessionLocal
from db.models import Book

"""
API Module

Exposes book data through a FastAPI service.
Connects to the database layer and provides endpoints to retrieve
and serve validated data from the pipeline.
"""

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Publishing Analytics API is running"}

@app.get("/books")
def get_books():
    session = SessionLocal()

    books = session.query(Book).all()

    result = []
    for book in books:
        result.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "sales": book.sales
        })

    session.close()

    return result

@app.get("/books/{book_id}")
def get_book(book_id: int):
    session = SessionLocal()

    book = session.query(Book).filter(Book.id == book_id).first()

    session.close()

    if not book:
        return {"error": "Book not found"}

    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "sales": book.sales
    }
