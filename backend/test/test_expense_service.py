from math import exp
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


def test_get_all_expenses(db_session):
    service = ExpenseService(db_session)

    service.create_expense(ExpenseCreate(title="A", amount=10, category="Food", date=date(2025,11,14)))
    service.create_expense(ExpenseCreate(title="B", amount=20, category="Bills", date=date(2025,11,15)))

    all_expenses = service.get_all_expenses()
    assert len(all_expenses) == 2
    titles = [e.title for e in all_expenses]
    assert "A" in titles
    assert "B" in titles

def test_get_expense(db_session):
    service = ExpenseService(db_session)
    expense = service.create_expense(ExpenseCreate(title="C", amount=30, category="Games", date=date(2025,11,16)))

    fetched = service.get_expense(expense.id)
    assert fetched.id == expense.id
    assert fetched.title == "C"

def test_update_expense(db_session):
    service = ExpenseService(db_session)
    expense= service.create_expense(ExpenseCreate(title="D", amount=40, category="Other", date=date(2025,11,16)))

    updated = service.update_expense(
        expense.id,
        ExpenseCreate(title="D-updated", amount=50, category="Other", date=date(2025,11,17))
    )
    assert updated.title == "D-updated"
    assert updated.amount == 50
    assert updated.date == date(2025,11,17)