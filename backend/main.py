from fastapi import FastAPI
from backend.database.database import Base, engine, init_db
from backend.expenses.expense_model import ExpenseModel
from backend.expenses.expense_router import router as expense_router
import os

app = FastAPI(title="ExpenseTracker")

# Initialize DB if not exists
init_db()

# Include routers
app.include_router(expense_router)

@app.get("/")
def root():
    return {"message": "Expense Tracker API działa!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
