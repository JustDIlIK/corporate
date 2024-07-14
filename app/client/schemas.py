from typing import Dict, List

from pydantic import BaseModel

from app.company.schemas import SCompany


class SClient(BaseModel):
    surname: Dict[str, str]
    firstname: Dict[str, str]
    photo_url: str
    company_id: int
    company: SCompany

    class Config:
        from_attributes = True


class SClientNotCompany(BaseModel):
    surname: Dict[str, str]
    firstname: Dict[str, str]
    photo_url: str
    company_id: int

    class Config:
        from_attributes = True


class SClientNotCompanyID(BaseModel):
    photo_url: str
    surname: Dict[str, str]
    firstname: Dict[str, str]


    class Config:
        from_attributes = True