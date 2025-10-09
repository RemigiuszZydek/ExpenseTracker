from sqlalchemy import create_engine 
import sqlalchemy
from sqlalchemy.orm import declarative_base 
import os

#SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./expenses.db"

#Create the database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#Base class for SQLalchemy models
Base = declarative_base()

#Metadata object (can be used for additional table configuration)
metadata = sqlalchemy.MetaData()

# Database init if database doesn't exists
def init_db():
    DB_PATH = "./expenses.db"

    if not os.path.exists(DB_PATH):
        print("📦 Tworzenie nowej bazy danych...")
        Base.metadata.create_all(bind=engine)
    else:
       pass