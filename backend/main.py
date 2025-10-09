from fastapi import FastAPI
from backend.database.database import Base, engine, init_db
from backend.database.models.expense_model import ExpenseModel
from backend.routers.expense_router import router as expense_router
import os

app = FastAPI(title="ExpenseTracker")

# Initialize DB if not exists
init_db()

# Include routers
app.include_router(expense_router)

@app.get("/")
def root():
    return {"message": "Expense Tracker API działa!"}

