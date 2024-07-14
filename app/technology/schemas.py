from typing import Dict, List

from pydantic import BaseModel


class STechnology(BaseModel):
    title: Dict[str, str]
    description: Dict[str, str]
    photo_url: str

    class Config:
        from_attributes = True
