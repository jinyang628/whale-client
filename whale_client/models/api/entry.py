from pydantic import BaseModel


class ApplicationRequest(BaseModel):
    name: str
    tables: list[dict]

class ApplicationResponse(BaseModel):
    id: str