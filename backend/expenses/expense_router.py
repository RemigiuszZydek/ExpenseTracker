from datetime import date, datetime
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from backend.database.database import  get_db_session
from .expense_schema import ExpenseCreate, ExpenseRead
from .expense_service import ExpenseService


# Create a new APIRouter instance with endpoint prefix /expenses
router = APIRouter(
    prefix="/expenses",
    tags = ["expenses"]
)

# Endpoint to create a new expense
# - Accepts data validated with ExpenseCreate schema
# - Returns data serialized with ExpenseRead schema

@router.get("/stats")
def get_expense_stats(
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    db: Session = Depends(get_db_session)
):
    expense_service = ExpenseService(db)
    stats = expense_service.get_stats(start_date=start_date, end_date=end_date)
    return stats

@router.post("/",response_model=ExpenseRead)
def create_expense(expense: ExpenseCreate, db: Session=Depends(get_db_session)):
    expense_service = ExpenseService(db)
    return expense_service.create_expense(expense)

@router.get("/",response_model=list[ExpenseRead])
def get_expenses(db: Session=Depends(get_db_session)):
    expense_service = ExpenseService(db)
    return expense_service.get_all_expenses()

@router.get("/{expense_id}", response_model=ExpenseRead)
def get_expense(expense_id: int, db: Session=Depends(get_db_session)):
    expense_service = ExpenseService(db)
    return expense_service.get_expense(expense_id)

@router.delete("/{expense_id}", response_model=ExpenseRead)
def delete_expense(expense_id: int, db: Session=Depends(get_db_session)):
    expense_service = ExpenseService(db)
    return expense_service.delete_expense(expense_id)
    
@router.put("/{expense_id}",response_model=ExpenseRead)
def update_expense(expense_id: int, updated_expense: ExpenseCreate, db: Session = Depends(get_db_session)):
    expense_service = ExpenseService(db)
    return expense_service.update_expense(expense_id, updated_expense)

@router.get("/filter", response_model=list[ExpenseRead])
def get_filtered_expenses(
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    min_amount: Optional[float] = Query(None),
    max_amount: Optional[float] = Query(None),
    category: Optional[str] = Query(None),
    db: Session = Depends(get_db_session)
):
    expense_service = ExpenseService(db)
    return expense_service.get_filtered_expenses(
        start_date=start_date,
        end_date=end_date,
        min_amount=min_amount,
        max_amount=max_amount,
        category=category
    )


