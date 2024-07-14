from datetime import datetime

from sqlalchemy import Column, Integer, String, Date, func, text

from app.database import Base


class Visitor(Base):
    __tablename__ = "visitors"

    id = Column(Integer, primary_key=True)
    ip_address = Column(String, nullable=False)
    cookie = Column(String, nullable=False)
    date = Column(Date, nullable=True)
