from sqlalchemy import Column, Integer, String, Float, DateTime,Date
from sqlalchemy.sql import func
from ..database.database import Base

#SQLalchemy model for "expenses" table
class ExpenseModel(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    amount = Column(Float,nullable=False)
    category = Column(String,nullable=False)
    date = Column(Date,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())