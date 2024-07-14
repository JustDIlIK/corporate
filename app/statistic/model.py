from datetime import datetime

from sqlalchemy import Column, Integer, String, Date, func, text

from app.database import Base


class Statistic(Base):
    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True)
    statistic_date = Column(Date, nullable=False)
    count = Column(Integer, nullable=False)