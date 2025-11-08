from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ExpenseTracker.backend.database.database import get_db_session
from ExpenseTracker.backend.database.schemas.income_schema import IncomeCreate, IncomeRead, IncomeSchema
from ExpenseTracker.backend.services.income_service import IncomeService



router = APIRouter(
    prefix="/income",
    tags=["income"]
)

@router.post("/",response_model=IncomeRead)
def create_income(income: IncomeCreate, db: Session=Depends(get_db_session)):
    income_service = IncomeService(db)
    return income_service.create_income(income)

