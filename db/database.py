from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base

# SQLite database (file will be created automatically)
DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(DATABASE_URL, echo = True)

SessionLocal = sessionmaker(bind=engine)

# Create tables based on the models
Base.metadata.create_all(bind=engine)