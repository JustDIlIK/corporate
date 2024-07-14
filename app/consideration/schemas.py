from fastapi import UploadFile
from pydantic import BaseModel, EmailStr, Field


class SConsideration(BaseModel):
    name: str
    phone: str = Field(pattern=r"^\+\d{7,}$")
    email: EmailStr
    description: str
    directions: str
    file: UploadFile

    class Config:
        from_attributes = True

