from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, JSON


class Lang(Base):
    __tablename__ = 'langs'

    id = Column(Integer, primary_key=True)
    lang_short = Column(JSON, nullable=False)
    lang_long = Column(JSON, nullable=False)

