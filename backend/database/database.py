from sqlalchemy import create_engine 
import sqlalchemy
from sqlalchemy.orm import declarative_base 
import os

SQLALCHEMY_DATABASE_URL = "sqlite:///./expenses.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Base = declarative_base()

metadata = sqlalchemy.MetaData()

def init_db():
    DB_PATH = "./expenses.db"

    if not os.path.exists(DB_PATH):
        print("📦 Tworzenie nowej bazy danych...")
        Base.metadata.create_all(bind=engine)
    else:
       pass