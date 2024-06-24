from enum import StrEnum
from pydantic import BaseModel
from typing import Optional

class DataType(StrEnum):
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    DATE = "date"
    DATETIME = "datetime"
    
class Column(BaseModel):
    name: str
    data_type: DataType
    nullable: bool = False

class Table(BaseModel):
    name: str
    description: Optional[str] = None
    schema: list[Column]