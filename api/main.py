from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from pipeline.ingest import load_data
from pipeline.validate import validate_schema, validate_business_rules
from pipeline.clean import clean_data
from db.insert import insert_books
from db.database import SessionLocal
from db.models import Book
from api.schemas import BookResponse

"""
API Module

Exposes book data through a FastAPI service.
Connects to the database layer and provides endpoints to retrieve
and serve validated data from the pipeline.
"""

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Publishing Analytics API is running"}

@app.get("/books", response_model=List[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book

@app.post("/ingest")
def ingest_data():
    df = load_data("data/raw/books_messy.csv")

    if df is None:
        raise HTTPException(status_code=400, detail="Failed to load data")
    
    df = validate_schema(df)

    if df is None:
        raise HTTPException(status_code=400, detail="Schema validation failed")
    
    df = clean_data(df)

    df = validate_business_rules(df)

    if df is None:
        raise HTTPException(status_code=400, detail="Business rules validation failed")
    
    df.to_csv("data/processed/books_cleaned.csv", index=False)

    insert_books(df)

    return {
        "message": "Data ingested and processed successfully",
        "rows_processed": len(df)
    }

@app.get("/analytics/top-selling", response_model=List[BookResponse])
def get_top_selling_books(db: Session = Depends(get_db)):
    top_books = db.query(Book).order_by(Book.sales.desc()).all()
    return top_books

