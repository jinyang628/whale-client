

from pydantic import BaseModel


class EntryRequest(BaseModel):
    application: list[dict]

class EntryResponse(BaseModel):
    id: str