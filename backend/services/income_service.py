from sqlalchemy.orm import Session
from sqlalchemy import func
from ExpenseTracker.backend.database.models.income_model import IncomeModel
from ExpenseTracker.backend.database.schemas.income_schema import IncomeCreate


class IncomeService:
    def __init__(self, db : Session) :
        self.db = db

    def create_income(self, income_data: IncomeCreate) -> IncomeModel:
        new_income = IncomeModel(**income_data.dict())
        self.db.add(new_income)
        self.db.commit()
        self.db.refresh(new_income)
        return new_income

    def get_all_incomes(self) -> list[IncomeModel]:
        return self.db.query(IncomeModel).all()
    
    def get_income(self, income_id: int) -> IncomeModel:
        return self.db.query(IncomeModel).filter(IncomeModel.id == income_id).first()
    
    def delete_income(self, income_id: int) -> IncomeModel:
        income = self.db.query(IncomeModel).filter(IncomeModel.id == income_id).first()
        if not income:
            raise Exception("Income not found")
        self.db.delete(income)
        self.db.commit()
        return income
    
    def update_income(self, income_id: int, updated_data: IncomeCreate) -> IncomeModel:
        income = self.db.query(IncomeModel).filter(IncomeModel.id == income_id).first()
        if not income:
            raise Exception("Income not found")
        for key,value in updated_data.dict().items():
            setattr(income,key,value)
        self.db.delete(income)
        self.db.commit()
        return income
    
    def get_average_income(self) -> float:
        avg_income = self.db.query(func.avg(IncomeModel)).scalar()
        return avg_income or 0.0