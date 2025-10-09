from pydantic import BaseModel
from datetime import date

# Pydantic schemas for expenses.
# - Used for validating incoming data (POST)
# - Used for serializing data sent to clients (GET)
class ExpenseSchema(BaseModel):
    title: str
    amount: float
    category: str
    date: date

class ExpenseCreate(ExpenseSchema):
    pass   # Inherits fields from ExpenseSchema for creating new expense

class ExpenseRead(ExpenseSchema):
    id: int
    created_at : date

    class Config:
        from_attributes = True      # Allows reading data from ORM models