from pydantic import BaseModel

from whale.models.database.table import Table

VERSION = "v1"

class ApiManager(BaseModel):
    
    tables: list[Table]
    base_path: str
    
    def __init__(self, tables: list[Table], api_key: str):
        table_names = [table.name for table in tables]
        if len(table_names) != len(set(table_names)):
            raise ValueError("Table names passed into ApiManager are not unique.")
        
        if not api_key:
            raise ValueError("API key is required.")
        
        self.tables = tables
        self.base_path = f"{api_key}/api/{VERSION}/"