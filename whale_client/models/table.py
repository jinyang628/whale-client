from enum import StrEnum
from pydantic import BaseModel, Field, model_validator
from typing import Optional, Any


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
    default_value: Optional[Any] = None

    @model_validator(mode="before")
    def set_default_value(self, values):
        if "nullable" in values and "default_value" not in values:
            nullable = values["nullable"]
            data_type = values["data_type"]
            if not nullable:
                if data_type == DataType.STRING:
                    values["default_value"] = ""
                elif data_type == DataType.INTEGER:
                    values["default_value"] = 0
                elif data_type == DataType.FLOAT:
                    values["default_value"] = 0.0
                elif data_type == DataType.BOOLEAN:
                    values["default_value"] = False
                elif data_type == DataType.DATETIME:
                    values["default_value"] = (
                        "1970-01-01T00:00:00Z"  # ISO format for datetime
                    )
        return values


class Table(BaseModel):
    name: str
    description: Optional[str] = None
    columns: list[Column]

    def __init__(self, **data):
        super().__init__(**data)
        self._validate_primary_key()

    def _validate_primary_key(self):
        primary_key_columns = [
            col for col in self.columns if col.primary_key != PrimaryKey.NONE
        ]
        if len(primary_key_columns) != 1:
            raise ValueError("Exactly one column must be set as primary key.")
