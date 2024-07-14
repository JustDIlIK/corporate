import os
from os import getcwd

from fastapi import UploadFile
from fastapi_storages import FileSystemStorage
from fastapi_storages.base import StorageFile
from fastapi_storages.integrations.sqlalchemy import ImageType, FileType
from sqlalchemy.event import listens_for
from sqlalchemy.orm import relationship

from app.config import settings
from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, JSON


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    surname = Column(JSON, nullable=False)
    firstname = Column(JSON, nullable=False)
    photo_abs = Column(FileType(storage=FileSystemStorage(path=f"{getcwd()}/media/clients")), nullable=True)
    photo_url = Column(String, nullable=True)
    company_id = Column(ForeignKey("companies.id", ondelete='SET NULL'), nullable=True)
    feedback = relationship("Feedback", backref="client")

    def __str__(self):
        return f"{self.surname['en']} {self.firstname['en']}"

# ImageType(storage=FileSystemStorage(path=f"{getcwd()}/media/clients"))


@listens_for(Client, 'before_insert')
def before_insert_listener(mapper, connection, target):
    target.photo_url = f"{settings.WEB_URL}/media/clients/{target.photo_abs.filename}"


@listens_for(Client, 'before_update')
def before_update_listener(mapper, connection, target):
    if not hasattr(target.photo_abs, "filename"):
        return

    if target.photo_abs.filename == "":
        return

    file_path = os.path.join(getcwd(), "media/clients", target.photo_abs.filename)
    with open(file_path, 'wb') as out_file:
        photo = target.photo_abs.file.read()
        out_file.write(photo)
    target.photo_url = f"{settings.WEB_URL}/media/clients/{target.photo_abs.filename}"


