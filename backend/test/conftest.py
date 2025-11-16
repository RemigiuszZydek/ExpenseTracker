from typing import final
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, false
from sqlalchemy.orm import sessionmaker
from backend.database.database import Base, get_db_session
from backend.main import app


SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session")
def create_test_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db_session] = override_get_db

@pytest.fixture
def db_session():
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    
    for table in reversed(Base.metadata.sorted_tables):
        session.execute(table.delete())
    session.commit()

    yield session
    session.close()
    
        
@pytest.fixture
def client():
    return TestClient(app)