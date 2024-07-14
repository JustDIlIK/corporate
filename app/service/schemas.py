from typing import Dict

from pydantic import BaseModel


class SService(BaseModel):
    title: Dict[str, str]
    description: Dict[str, str]
    price: int

    class Config:
        from_attributes = True
