from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database.database import engine, Base, SessionLocal, get_db_session
from backend.database.models.expense_model import ExpenseModel
from backend.database.schemas.expense_schema import ExpenseCreate, ExpenseRead

# Create a new APIRouter instance with endpoint prefix /expenses
router = APIRouter(
    prefix="/expenses",
    tags = ["expenses"]
)

# Endpoint to create a new expense
# - Accepts data validated with ExpenseCreate schema
# - Returns data serialized with ExpenseRead schema

@router.post("/",response_model=ExpenseRead)
def create_expense(expense: ExpenseCreate, db: Session=Depends(get_db_session)):
    # Create a new instance of the ExpenseModel using data from the request
    db_expense = ExpenseModel(**expense.dict())
     # Add the new expense to the session (staging it for insertion into the database)
    db.add(db_expense)
    # Commit the session to save changes into the database
    db.commit()
    # Refresh the object to get updated fields (like auto-generated id and created_at)
    db.refresh(db_expense)
    # Return the newly created expense as response
    return db_expense

@router.get("/",response_model=list[ExpenseRead])
def get_expense(db: Session=Depends(get_db_session)):
    expenses = db.query(ExpenseModel).all()
    return expenses

