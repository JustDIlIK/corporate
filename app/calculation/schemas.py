from typing import Dict

from pydantic import BaseModel, json


class SCalculation(BaseModel):

    title: Dict[str, str]
    description: Dict[str, str]
    services_id: int

    class Config:
        from_attributes = True

