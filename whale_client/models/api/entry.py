from pydantic import BaseModel


class PostApplicationRequest(BaseModel):
    name: str
    tables: list[dict]


class PostApplicationResponse(BaseModel):
    name: str
