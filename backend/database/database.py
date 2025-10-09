from sqlalchemy import create_engine 
import sqlalchemy
from sqlalchemy.orm import declarative_base,sessionmaker, Session
import os
from typing import Generator

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

#Create a sessionmaker bound to the engine
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# Database init if database doesn't exists
def init_db():
    DB_PATH = "./expenses.db"

    if not os.path.exists(DB_PATH):
        print("📦 Tworzenie nowej bazy danych...")
        Base.metadata.create_all(bind=engine)
    else:
       pass


# Dependency function to get a database session
# This function will be used with FastAPI's Depends system
def get_db_session() -> Generator[Session, None, None]:
    db = SessionLocal() # Create a new database session
    try:
        yield db # Provide the session to the endpoint
    finally:
        db.close() # Close the session after the request is done