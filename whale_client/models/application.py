from dataclasses import dataclass
from whale_client.models.table import Table

VERSION = "v1"

@dataclass
class Application:
    
    _name: str
    _tables: list[Table]
    
    def __init__(self, name, tables: list[Table]):
        table_names = [table.name for table in tables]
        if len(table_names) != len(set(table_names)):
            raise ValueError("Table names passed into Application are not unique.")
        self._name = name
        self._tables = tables
        
    @property  
    def name(self) -> str:
        return self._name
    
    @property
    def tables(self) -> list[Table]:
        return self._tables
        
    def __str__(self):
        return f"Application ({self.name}) contains {len(self.tables)} tables: {', '.join([table.name for table in self.tables])}"