from typing import Optional
from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.database.models.expense_model import ExpenseModel
from backend.database.schemas.expense_schema import ExpenseCreate

class ExpenseService:
    def __init__(self, db : Session):
        self.db = db

    def create_expense(self, expense_data: ExpenseCreate) -> ExpenseModel:
        new_expense = ExpenseModel(**expense_data.dict())
        self.db.add(new_expense)
        self.db.commit()
        self.db.refresh(new_expense)
        return new_expense
    
    def get_all_expenses(self) -> list[ExpenseModel]:
        return self.db.query(ExpenseModel).all()
    
    def delete_expense(self, expense_id: int) -> ExpenseModel:
        expense = self.db.query(ExpenseModel).filter(ExpenseModel.id == expense_id).first()
        if not expense:
            raise Exception("Expense not found")
        self.db.delete(expense)
        self.db.commit()
        return expense
    
    def update_expense(self, expense_id: int, updated_data:ExpenseCreate) -> ExpenseModel:
        expense = self.db.query(ExpenseModel).filter(ExpenseModel.id == expense_id).first()
        if not expense:
            raise Exception("Expense not found")
        for key,value in updated_data.dict().items():
            setattr(expense,key,value)
        self.db.commit()
        self.db.refresh(expense)
        return expense
    
    def get_filtered_expenses(self,
                              start_date: Optional[date] = None,
                              end_date: Optional[date] = None,
                              category: Optional[str] = None,
                              min_amount: Optional[float] = None,
                              max_amount: Optional[float] = None) -> list[ExpenseModel]:
        """Gives back filtered list of expenses"""
        query = self.db.query(ExpenseModel)
        if start_date:
            query = query.filter(ExpenseModel.date >= start_date)
        if end_date:
            query = query.filter(ExpenseModel.date <= end_date)
        if category:
            query = query.filter(ExpenseModel.category == category)
        if min_amount:
            query = query.filter(ExpenseModel.amount >= min_amount)
        if max_amount:
            query = query.filter(ExpenseModel.amount <= max_amount)
        return query.all()
    
    def get_stats(self, start_date: Optional[date] = None, end_date: Optional[date] = None):
        """Returns sum, average by categories"""
        query = self.db.query(ExpenseModel)

        if start_date:
            query = query.filter(ExpenseModel.date >= start_date)
        if end_date:
            query = query.filter(ExpenseModel.date <= end_date)

        total = self.db.query(func.sum(ExpenseModel.amount)).scalar() or 0.0

        if not start_date or not end_date:
            first_date = self.db.query(func.min(ExpenseModel.date)).scalar()
            last_date = self.db.query(func.max(ExpenseModel.date)).scalar()
        else:
            first_date, last_date = start_date, end_date

        if first_date and last_date:
            days = (last_date - first_date).days + 1
            average_per_day = total / days if days > 0 else 0
        else:
            average_per_day = 0

        by_category_query = (
            self.db.query(ExpenseModel.category, func.sum(ExpenseModel.amount))
            .group_by(ExpenseModel.category)
            .all()
        )
        by_category = {cat: float(amount) for cat, amount in by_category_query}

        return {
            "total": float(total),
            "average_per_day": round(average_per_day, 2),
            "by_category": by_category
        }