from sqlalchemy.event import listens_for

from app.database import Base
from sqlalchemy import Column, String, Integer, JSON


class Achievement(Base):
    __tablename__ = "achievements"

    id = Column(Integer, primary_key=True)
    description = Column(JSON, nullable=False)
    value = Column(Integer, nullable=False)


