import os
import shutil
from pathlib import Path
from typing import Optional
from fastapi import APIRouter, UploadFile, File, Body, Form
from pydantic import EmailStr
from starlette import status
from starlette.responses import JSONResponse

from app.consideration.dao import ConsiderationDAO
from app.consideration.schemas import SConsideration

router = APIRouter(
    prefix="/considerations",
    tags=["Заявки"]
)


@router.post("")
async def create_consideration(name: str = Form(...),
                               phone: str = Form(..., regex=r"\+\d{8,}"),
                               email: EmailStr = Form(...),
                               description: str = Form(...),
                               directions: str = Form(...),
                               file: Optional[UploadFile] = File(None)):
	
    consideration = await ConsiderationDAO.add_consideration(name=name,
                                                             phone=phone,
                                                             email=email,
                                                             description=description,
                                                             directions=directions,
                                                             file=file)

    if not consideration:
        return JSONResponse({"detail": "Не удалось отправить заявку"}, status_code=status.HTTP_409_CONFLICT)

    return  JSONResponse({"detail": "Успешное добавление удалось отправить заявку"})



