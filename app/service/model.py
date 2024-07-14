from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, JSON


class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    title = Column(JSON, nullable=False)
    description = Column(JSON, nullable=False)
    price = Column(Integer, nullable=False)
    calculation_id = Column(ForeignKey('calculations.id', ondelete='SET NULL'), nullable=True)

    def __str__(self):
        return self.title["en"]
