from sqlalchemy.orm import Session
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
    
