from sqlalchemy import Column, Integer, Nullable, String, DateTime, Date, Float, func
from ..database import Base
class IncomeModel(Base):
    __tablename__ = "income"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    amount = Column(Float,nullable=False)
    date = Column(Date,nullable=False)
    creadet_at = Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())