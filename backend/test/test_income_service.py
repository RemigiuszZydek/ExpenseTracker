from backend.income.income_service import IncomeService
from backend.income.income_schema import IncomeCreate
from backend.income.income_model import IncomeModel
from datetime import date

def test_add_income(db_session):
    service = IncomeService(db_session)

    income = IncomeCreate(
        title="Test income",
        amount=100,
        date=date(2025,11,14)
    )

    new_income = service.create_income(income)
    assert isinstance(new_income, IncomeModel)
    assert new_income.id is not None
    assert new_income.title == "Test income"
    assert new_income.amount == 100
    assert str(new_income.date) == "2025-11-14"

    saved = db_session.query(IncomeModel).order_by(IncomeModel.id.desc()).first()
    assert saved.id == new_income.id
    assert saved.title == "Test income"

def test_get_all_incomes(db_session):
    service = IncomeService(db_session)

    service.create_income(IncomeCreate(title="A", amount=50, date=date(2025,11,15)))
    service.create_income(IncomeCreate(title="B", amount=60, date=date(2025,11,16)))

    all_incomes = service.get_all_incomes()
    assert len(all_incomes) == 2
    titles = [e.title for e in all_incomes]
    assert "A" in titles
    assert "B" in titles

def test_get_income(db_session):
    service = IncomeService(db_session)
    income = service.create_income(IncomeCreate(title="C", amount=70, date=date(2025,11,17)))

    fetched = service.get_income(income.id)
    assert fetched.id == income.id
    assert fetched.title == "C"

def test_update_expense(db_session):
    service = IncomeService(db_session)
    income = service.create_income(IncomeCreate(title="D", amount=80, date=date(2025,11,18)))

    updated = service.update_income(
        income.id,
        IncomeCreate(title="D-updated", amount=90, date=date(2025,11,19))
    )

    assert updated.title == "D-updated"
    assert updated.amount == 90
    assert updated.date == date(2025,11,19)

def test_delete_expense(db_session):
    service = IncomeService(db_session)
    income = service.create_income(IncomeCreate(title="F", amount=100, date=date(2025,11,20)))

    deleted = service.delete_income(income.id)
    assert deleted.id == income.id
    assert service.get_income(income.id) is None

def test_get_average_income(db_session):
    service = IncomeService(db_session)
    service.create_income(IncomeCreate(title="I", amount=10,  date=date(2025,11,22)))
    service.create_income(IncomeCreate(title="J", amount=20,  date=date(2025,11,23)))
    service.create_income(IncomeCreate(title="K", amount=30,  date=date(2025,11,24)))

    avg = service.get_average_income()

    assert avg == 20.00