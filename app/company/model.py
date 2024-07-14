import os

from sqlalchemy.event import listens_for
from sqlalchemy.orm import relationship

from app.config import settings
from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, JSON, Boolean
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType, FileType
from os import getcwd


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    title = Column(JSON, nullable=False)
    description = Column(JSON, nullable=False)
    photo_abs = Column(FileType(storage=FileSystemStorage(path=f"{getcwd()}/media/companies")), nullable=True)
    photo_url = Column(String, nullable=True)
    is_partner = Column(Boolean, nullable=True, default=False)
    is_client = Column(Boolean, nullable=True, default=False)
    client = relationship("Client", backref="company")

    def __str__(self):
        return self.name

# ImageType(storage=FileSystemStorage(path=f"{getcwd()}/media/companies"))/


@listens_for(Company, 'before_insert')
def before_insert_listener(mapper, connection, target):
    target.photo_url = f"{settings.WEB_URL}/media/companies/{target.photo_abs.filename}"


@listens_for(Company, 'before_update')
def before_update_listener(mapper, connection, target):
    if not hasattr(target.photo_abs, "filename"):
        return
    if target.photo_abs.filename == "":
        return

    file_path = os.path.join(getcwd(), "media/companies", target.photo_abs.filename)
    with open(file_path, 'wb') as out_file:
        photo = target.photo_abs.file.read()
        out_file.write(photo)
    target.photo_url = f"{settings.WEB_URL}/media/companies/{target.photo_abs.filename}"
