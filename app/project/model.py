import os
from os import getcwd
from typing import List

from fastapi_storages import FileSystemStorage, StorageFile
from fastapi_storages.integrations.sqlalchemy import ImageType, FileType
from sqlalchemy.event import listens_for
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.orm.exc import FlushError
from sqlalchemy.testing import db

from app.config import settings
from app.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, JSON, Boolean


class Project(Base):
    __tablename__ = "projects"

    id = mapped_column(Integer, primary_key=True)

    name = Column(JSON, nullable=False)
    title = Column(JSON, nullable=False)
    description = Column(JSON, nullable=False)
    category_id = Column(ForeignKey("directions.id", ondelete='SET NULL'), nullable=True)
    link = Column(String, nullable=True)
    feedback_id = Column(ForeignKey("feedbacks.id", ondelete='SET NULL'), nullable=True)
    images: Mapped[List["ProjectImage"]] = relationship()

    def __str__(self):
        return self.name["en"]


class ProjectImage(Base):
    __tablename__ = "projects_image"

    id = mapped_column(Integer, primary_key=True)
    photo_abs = Column(FileType(storage=FileSystemStorage(path=f"{getcwd()}/media/projects")), nullable=True)
    photo_url = Column(String, nullable=True)
    result = Column(Boolean, default=False)
    parent_id: Mapped[int] = mapped_column(ForeignKey("projects.id", ondelete='SET NULL'), nullable=True)

    def __str__(self):
        return self.photo_url


# ImageType(storage=FileSystemStorage(path=f"{getcwd()}/media/projects"))


@listens_for(ProjectImage, 'before_insert')
def before_insert_listener(mapper, connection, target):

    if target.photo_abs.filename is None:
        raise FlushError("Произошла ошибка, запись не будет добавлена в базу данных")
    if target.photo_abs.filename == "":
        raise FlushError("Произошла ошибка, запись не будет добавлена в базу данных")

    target.photo_url = f"{settings.WEB_URL}/media/projects/{target.photo_abs.filename}"


@listens_for(ProjectImage, 'before_update')
def before_update_listener(mapper, connection, target):
    if not hasattr(target.photo_abs, "filename"):
        return

    if target.photo_abs is None:
        return
        raise FlushError("Произошла ошибка, запись не будет добавлена в базу данных")
    elif target.photo_abs.filename == "":
        if target.photo_url != "":
            target.photo_abs.filename = target.photo_url
        else:
            raise FlushError("Произошла ошибка, запись не будет добавлена в базу данных")

    file_path = os.path.join(getcwd(), "media/projects", target.photo_abs.filename)
    with open(file_path, 'wb') as out_file:
        photo = target.photo_abs.file.read()
        out_file.write(photo)
    target.photo_url = f"{settings.WEB_URL}/media/projects/{target.photo_abs.filename}"



