from enum import StrEnum
from typing import Optional, Any
from pydantic import BaseModel, model_validator
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class DataType(StrEnum):
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    DATE = "date"
    # DATETIME = "datetime"
    UUID = "uuid"
    ENUM = "enum"


class PrimaryKey(StrEnum):
    AUTO_INCREMENT = "auto_increment"
    UUID = "uuid"


class ForeignKey(BaseModel):
    table: str
    column: str


class Column(BaseModel):
    name: str
    data_type: DataType
    enum_values: Optional[list[str]] = None
    nullable: bool = False
    default_value: Optional[Any] = None
    unique: Optional[bool] = False
    foreign_key: Optional[ForeignKey] = None

    @model_validator(mode="before")
    @classmethod
    def set_default_value(cls, data: Any) -> Any:

        if not isinstance(data, dict):
            raise ValueError("Column data must be a dictionary.")

        cls._validate_enum_values(data)
        cls._set_default_value(data)

        return data

    @staticmethod
    def _validate_enum_values(data: dict) -> None:
        if data.get('data_type') == DataType.ENUM:
            if data.get("enum_values") is None:
                raise ValueError("enum_values must be set for columns with data type 'enum'.")
            if not data.get("enum_values"):
                raise ValueError("enum_values cannot be empty.")
            if len(data.get("enum_values")) != len(set(data.get("enum_values"))):
                raise ValueError("enum_values must be unique.")
            
            non_string_values = [v for v in data.get('enum_values') if not isinstance(v, str)]
            if non_string_values:
                raise ValueError(f"All enum_values must be of type string. Non-string values found: {non_string_values}")
            
            if data.get('default_value') not in data.get("enum_values"):
                raise ValueError("default_value must be one of the enum_values.")
        else:
            if data.get("enum_values"):
                raise ValueError("enum_values can only be set for columns with data type 'enum'.")
    
    @staticmethod
    def _set_default_value(data: dict) -> None:
        # If the default value is set, use it
        if "default_value" in data:
            return

        data_type = data["data_type"]
        if data_type == DataType.STRING:
            data["default_value"] = ""
        elif data_type == DataType.INTEGER:
            data["default_value"] = 0
        elif data_type == DataType.FLOAT:
            data["default_value"] = 0.0
        elif data_type == DataType.BOOLEAN:
            data["default_value"] = False

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
    primary_key: PrimaryKey = PrimaryKey.AUTO_INCREMENT
    enable_created_at_timestamp: Optional[bool] = False
    enable_updated_at_timestamp: Optional[bool] = False

    def __init__(self, **data):
        super().__init__(**data)
        self._validate_name()

    def _validate_name(self):
        if not self.name:
            raise ValueError("Table name cannot be empty.")

        if not self.name.islower():
            raise ValueError("All characters in table name must be in lower case.")

        if " " in self.name:
            raise ValueError("Table name cannot contain spaces.")
