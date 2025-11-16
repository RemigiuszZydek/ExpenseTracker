from backend.expenses.expense_service import ExpenseService
from backend.expenses.expense_schema import ExpenseCreate
from backend.expenses.expense_model import ExpenseModel
from datetime import date

def test_add_expense(db_session):
    service = ExpenseService(db_session)

    expense = ExpenseCreate(
        title="Test service expense",
        amount=500,
        category="Food",
        date=date(2025,11,14)
    )

    new_expense = service.create_expense(expense)

    assert isinstance(new_expense, ExpenseModel)
    assert new_expense.id is not None
    assert new_expense.title == "Test service expense"
    assert new_expense.amount == 500
    assert new_expense.category == "Food"
    assert str(new_expense.date) == "2025-11-14"

    saved = db_session.query(ExpenseModel).order_by(ExpenseModel.id.desc()).first()
    assert saved.id == new_expense.id
    assert saved.title == "Test service expense"


