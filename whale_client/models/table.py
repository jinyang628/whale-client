from enum import StrEnum
from pydantic import BaseModel
from typing import Optional

# TODO: Expand the valid data types as per SQLAlchemy/SQLite's valid data types
class DataType(StrEnum):
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    DATETIME = "datetime"
    
# TODO: Add more types, e.g. UUID, etc. Will handle the id generation in house in server
# TODO: Some of the primary key types require the column to be a particular data type. E.g. AUTO_INCREMENT requires the column to be an integer
class PrimaryKey(StrEnum):
    NONE = "none" 
    AUTO_INCREMENT = "auto_increment"
    
class Column(BaseModel):
    name: str
    data_type: DataType
    primary_key: PrimaryKey = PrimaryKey.NONE
    nullable: bool = False

class Table(BaseModel):
    name: str
    description: Optional[str] = None
    columns: list[Column]
    
    def __init__(self, **data):
        super().__init__(**data)
        self._validate_primary_key()

    def _validate_primary_key(self):
        primary_key_columns = [col for col in self.columns if col.primary_key != PrimaryKey.NONE]
        if len(primary_key_columns) != 1:
            raise ValueError("Exactly one column must be set as primary key.")
