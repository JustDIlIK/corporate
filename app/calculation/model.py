from sqlalchemy.orm import mapped_column, relationship

from app.database import Base
from sqlalchemy import Column, Integer, JSON, String, ForeignKey


class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True)
    title = Column(JSON, nullable=False)
    description = Column(JSON, nullable=False)
    services = relationship("Service", backref="calculation")

    def __str__(self):
        return self.title["en"]
