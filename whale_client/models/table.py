from enum import StrEnum
from typing import Optional, Any
from pydantic import BaseModel, model_validator


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


class ForeignKey(BaseModel):
    table: str
    column: str


class Column(BaseModel):
    name: str
    data_type: DataType
    primary_key: PrimaryKey = PrimaryKey.NONE
    nullable: bool = False
    default_value: Optional[Any] = None
    unique: Optional[bool] = False
    foreign_key: Optional[ForeignKey] = None

    @model_validator(mode="before")
    @classmethod
    def set_default_value(cls, data: Any) -> Any:

        if not isinstance(data, dict):
            raise ValueError("Column data must be a dictionary.")

        # If the default value is set, use it
        if "default_value" in data:
            return data

        if "nullable" in data:
            if data["nullable"]:
                # If the column is nullable, the default value is None
                return data

        data_type = data["data_type"]
        if data_type == DataType.STRING:
            data["default_value"] = ""
        elif data_type == DataType.INTEGER:
            data["default_value"] = 0
        elif data_type == DataType.FLOAT:
            data["default_value"] = 0.0
        elif data_type == DataType.BOOLEAN:
            data["default_value"] = False
        elif data_type == DataType.DATETIME:
            data["default_value"] = "1970-01-01T00:00:00Z"  # ISO format for datetime

        return data

    def __init__(self, **data):
        super().__init__(**data)
        self._validate_name()

    def _validate_name(self):
        if not self.name: 
            raise ValueError("Column name cannot be empty.")
        
        if not self.name.islower():
            raise ValueError("All characters in column name must be in lower case.")
        
        if " " in self.name:
            raise ValueError("Column name cannot contain spaces.")


class Table(BaseModel):
    name: str
    description: Optional[str] = None
    columns: list[Column]

    def __init__(self, **data):
        super().__init__(**data)
        self._validate_primary_key()
        self._validate_name()

    def _validate_primary_key(self):
        primary_key_columns = [
            col for col in self.columns if col.primary_key != PrimaryKey.NONE
        ]
        if len(primary_key_columns) != 1:
            raise ValueError("Exactly one column must be set as primary key.")

    def _validate_name(self):
        if not self.name: 
            raise ValueError("Table name cannot be empty.")
        
        if not self.name.islower():
            raise ValueError("All characters in table name must be in lower case.")
        
        if " " in self.name:
            raise ValueError("Table name cannot contain spaces.")
