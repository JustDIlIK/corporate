import os

from sqlalchemy.event import listens_for

from app.config import settings
from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, String, JSON

from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType, FileType
from os import getcwd


class Technology(Base):
    __tablename__ = 'technologies'

    id = Column(Integer, primary_key=True)
    title = Column(JSON, nullable=False)
    description = Column(JSON, nullable=False)
    photo_abs = Column(FileType(storage=FileSystemStorage(path=f"{getcwd()}/media/technologies")), nullable=True)
    photo_url = Column(String, nullable=True)

    def __str__(self):
        return self.title["en"]


# Column(FileType(storage=FileSystemStorage(path=f"{getcwd()}/media/technologies")), nullable=False)


@listens_for(Technology, 'before_insert')
def before_insert_listener(mapper, connection, target):
    target.photo_url = f"{settings.WEB_URL}/media/technologies/{target.photo_abs.filename}"


@listens_for(Technology, 'before_update')
def before_update_listener(mapper, connection, target):
    if not hasattr(target.photo_abs, "filename"):
        return
    if target.photo_abs.filename == "":
        return

    file_path = os.path.join(getcwd(), "media/technologies", target.photo_abs.filename)
    with open(file_path, 'wb') as out_file:
        photo = target.photo_abs.file.read()
        out_file.write(photo)
    target.photo_url = f"{settings.WEB_URL}/media/technologies/{target.photo_abs.filename}"