from db.database import SessionLocal
from db.models import Book

def insert_books(df):
    session = SessionLocal()

    for _, row in df.iterrows():
        book = Book(
            id=int(row["id"]),
            title=row["title"],
            author=row["author"],
            sales=float(row["sales"])
        )
        session.add(book)

    session.commit()
    session.close()

    print("[INFO] Data inserted into the database")