from pydantic import BaseModel
from datetime import date, datetime

# Pydantic schemas for income.
# - Used for validating incoming data (POST)
# - Used for serializing data sent to clients (GET)

class IncomeSchema(BaseModel):
    tittle: str
    amount: float
    date: date

class IncomeCreate(IncomeSchema):
    pass    # Inherits fields from IncomeSchema for creating new expense

class IncomeRead(IncomeSchema):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Allows reading data from ORM models