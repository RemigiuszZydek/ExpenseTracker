from turtle import reset, title
from backend.expenses.expense_model import ExpenseModel
from datetime import date

def test_create_and_query_expense_in_db(db_session):
    expense = ExpenseModel(
        title="Test expense",
        amount=100.5,
        category="Test",
        date=date(2025,11,13)
    )

    db_session.add(expense)
    db_session.commit()

    result = db_session.query(ExpenseModel).first()
    assert result.title == "Test expense"
    assert result.amount == 100.5
    assert result.category == "Test"

    