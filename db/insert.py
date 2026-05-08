from db.database import SessionLocal
from db.models import Book

"""
Data Insertion Module

Handles inserting and updating records in the database.
Implements idempotent logic to prevent duplicate entries by updating
existing records when they already exist.
"""

def insert_books(df):
    session = SessionLocal()

    try:
        for _, row in df.iterrows():
            existing_book = session.query(Book).filter(Book.id == int(row["id"])).first()

            if existing_book:
                existing_book.title = row["title"]
                existing_book.author = row["author"]
                existing_book.sales = float(row["sales"])
            else:
                book = Book(
                    id=int(row["id"]),
                    title=row["title"],
                    author=row["author"],
                    sales=float(row["sales"])
                )
                session.add(book)

        session.commit()

        print("[INFO] Data inserted/updated into the database")

    except Exception as e:
        session.rollback()
        print(f"[ERROR] Failed to insert data into the database: {e}")
        
    finally:
        session.close()