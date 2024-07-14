import os

from sqlalchemy.event import listens_for

from app.config import settings
from app.database import Base
from sqlalchemy import Column, Integer, JSON, String
from os import getcwd
from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType, FileType


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    full_name = Column(JSON, nullable=False)
    position = Column(JSON, nullable=False)
    description = Column(JSON, nullable=False)
    stack = Column(String, nullable=False)
    experience = Column(JSON, nullable=False)
    education = Column(JSON, nullable=False)
    photo_abs = Column(FileType(storage=FileSystemStorage(path=f"{getcwd()}/media/employees")), nullable=True)
    photo_url = Column(String, nullable=True)



    def __str__(self):
        return self.full_name["en"]
# ImageType(storage=FileSystemStorage(path=f"{getcwd()}/media/employees"))


@listens_for(Employee, 'before_insert')
def before_insert_listener(mapper, connection, target):
    target.photo_url = f"{settings.WEB_URL}/media/employees/{target.photo_abs.filename}"


@listens_for(Employee, 'before_update')
def before_update_listener(mapper, connection, target):
    if not hasattr(target.photo_abs, "filename"):
        return
    if target.photo_abs.filename == "":
        return

    file_path = os.path.join(getcwd(), "media/employees", target.photo_abs.filename)
    with open(file_path, 'wb') as out_file:
        photo = target.photo_abs.file.read()
        out_file.write(photo)
    target.photo_url = f"{settings.WEB_URL}/media/employees/{target.photo_abs.filename}"