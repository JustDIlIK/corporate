from typing import Dict, List

from pydantic import BaseModel


class SCompany(BaseModel):

    name: str
    title: Dict[str, str]
    description: Dict[str, str]
    photo_url: str
    is_partner: bool
    is_client: bool

    class Config:
        from_attributes = True
