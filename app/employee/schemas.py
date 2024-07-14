from typing import Dict

from pydantic import BaseModel, json


class SEmployee(BaseModel):

    full_name: Dict[str, str]
    position: Dict[str, str]
    description: Dict[str, str]
    stack: str
    experience: Dict[str, str]
    education: Dict[str, str]
    photo_url: str

    class Config:
        from_attributes = True

