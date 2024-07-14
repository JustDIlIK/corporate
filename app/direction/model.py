from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, Integer, JSON


class Direction(Base):
    __tablename__ = 'directions'

    id = Column(Integer, primary_key=True)
    content = Column(JSON, nullable=False)
    project = relationship("Project", backref="direction")


    def __str__(self):
        return self.content["en"]