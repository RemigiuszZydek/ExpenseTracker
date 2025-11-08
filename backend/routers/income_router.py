from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ExpenseTracker.backend.database.database import get_db_session
from ExpenseTracker.backend.database.models.income_model import IncomeModel
from ExpenseTracker.backend.database.schemas.income_schema import IncomeCreate, IncomeRead, IncomeSchema
from ExpenseTracker.backend.services import income_service
from ExpenseTracker.backend.services.income_service import IncomeService



router = APIRouter(
    prefix="/income",
    tags=["income"]
)

@router.post("/",response_model=IncomeRead)
def create_income(income: IncomeCreate, db: Session=Depends(get_db_session)):
    income_service = IncomeService(db)
    return income_service.create_income(income)

@router.get("/",response_model=list[IncomeRead])
def get_incomes(db: Session=Depends(get_db_session)):
    income_service = IncomeService(db)
    return income_service.get_all_incomes()

@router.get("/{income_id}",response_model=IncomeRead)
def get_income(income_id: int, db: Session=Depends(get_db_session)):
    income_service = IncomeService(db)
    return income_service.get_income(income_id)

@router.delete("/{income_ide}", response_model= IncomeRead)
def delete_income(income_id: int, db: Session=Depends(get_db_session)):
    income_service = IncomeService(db)
    return income_service.delete_income(income_id)

@router.put("/{income_id}",response_model= IncomeRead)
def update_income(income_id: int, updated_income: IncomeCreate, db: Session=Depends(get_db_session)):
    income_service = IncomeService(db)
    return income_service.update_income(income_id, updated_income)

@router.get("/average")
def get_average(db: Session=Depends(get_db_session)):
    income_service = IncomeService(db)
    return income_service.get_average_income()
