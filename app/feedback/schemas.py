from typing import Dict, List

from pydantic import BaseModel, json

from app.client.schemas import SClient, SClientNotCompany, SClientNotCompanyID


class SFeedback(BaseModel):
    client_id: int
    content: Dict[str, str]
    client: SClientNotCompany

    class Config:
        from_attributes = True


class SFeedback2(BaseModel):
    client_id: int
    content: Dict[str, str]
    client: SClientNotCompanyID

    class Config:
        from_attributes = True