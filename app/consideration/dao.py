import os
import shutil
from pathlib import Path

from sqlalchemy import insert

from app.consideration.model import Consideration
from app.dao.base import BaseDAO
from app.database import async_session_maker


class ConsiderationDAO(BaseDAO):
    model = Consideration

    @classmethod
    async def add_consideration(cls, **data):
        if data['file'] is not None:
            url = f"{os.getcwd()}/media/considerations"

            upload_folder = Path(url)
            upload_folder.mkdir(parents=True, exist_ok=True)

            filename = data['file'].filename
            file_path = upload_folder / filename

            with file_path.open("wb") as f:
                shutil.copyfileobj(data['file'].file, f)

            data['file'] = f"{url}/{filename}"
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data).returning(cls.model)
            result = await session.execute(query)
            await session.commit()
            return result.first()


