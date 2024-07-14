from datetime import datetime

from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType
from sqlalchemy import Column, Integer, String, JSON, Date, LargeBinary

from app.database import Base


class Consideration(Base):
    __tablename__ = "considerations"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    description = Column(String, nullable=False)
    directions = Column(JSON, nullable=False)
    file = Column(String, nullable=True)
    created_at = Column(Date, default=datetime.now().date())