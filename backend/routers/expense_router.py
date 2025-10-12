from math import exp
from fastapi import APIRouter, Depends, HTTPException
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



@router.delete("/{expense_id}", response_model=ExpenseRead)
def delete_expense(expense_id: int, db: Session=Depends(get_db_session)):
    # Delete expense by id
    db_expense = db.query(ExpenseModel).filter(ExpenseModel.id == expense_id).first()
    
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    db.delete(db_expense)
    db.commit()

    return {"message": f"Expense with id {expense_id} deleted successfully"}
    

@router.put("/{expense_id}",response_model=ExpenseRead)
def update_expense(expense_id: int, updated_expense: ExpenseCreate, db: Session = Depends(get_db_session)):
    db_expense = db.query(ExpenseModel).filter(ExpenseModel.id == expense_id).first()
    # Find expense by ID
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    # Update each field
    for key,value in updated_expense.dict().items():
        setattr(db_expense,key,value)

    db.commit()
    db.refresh(db_expense)
    return db_expense