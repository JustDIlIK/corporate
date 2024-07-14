from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, JSON


class Feedback(Base):
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True)
    client_id = Column(ForeignKey("clients.id", ondelete='SET NULL'), nullable=True)
    content = Column(JSON, nullable=False)
    project = relationship("Project", backref="feedback")


    def __str__(self):
        return self.content["en"]