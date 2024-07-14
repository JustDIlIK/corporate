from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, JSON


class Feature(Base):
    __tablename__ = 'features'

    id = Column(Integer, primary_key=True)
    title = Column(JSON, nullable=False)
    description = Column(JSON, nullable=False)
