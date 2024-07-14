from typing import Dict, Any

from pydantic import BaseModel, EmailStr


class SUsersAuth(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True