from fastapi import FastAPI
from backend.database.database import Base, engine, init_db
from backend.database.models.expense_model import ExpenseModel
import os

app = FastAPI(title="ExpenseTracker")


init_db()


@app.get("/")
def root():
    return {"message": "Expense Tracker API działa!"}

