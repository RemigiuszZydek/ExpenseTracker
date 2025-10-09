from pydantic import BaseModel
from datetime import date

class ExpenseSchema(BaseModel):
    title: str
    amount: float
    category: str
    date: date

class ExpenseCreate(ExpenseSchema):
    pass

class ExpenseRead(ExpenseSchema):
    id: int
    created_at : date

    class Config:
        from_attributes = True