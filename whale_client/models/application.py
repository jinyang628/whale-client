from dataclasses import dataclass
from whale_client.models.table import Table

VERSION = "v1"

@dataclass
class Application:
    
    _name: str
    _tables: list[Table]
    
    def __init__(self, name: str, tables: list[Table]):
        self._name = name
        self._tables = tables
        self._validate_name()
        self._validate_tables()
        
        
    def _validate_name(self):
        if not self._name: 
            raise ValueError("Application name cannot be empty.")
        
        if not self._name.islower():
            raise ValueError("All characters in application name must be in lower case.")
        
        if " " in self._name:
            raise ValueError("Application name cannot contain spaces.")
        
    def _validate_tables(self):
        if not self._tables:
            raise ValueError("Application must contain at least one table.")
        
        table_names = [table.name for table in self._tables]
        if len(table_names) != len(set(table_names)):
            raise ValueError("Table names passed into Application are not unique.")
        
        
    @property  
    def name(self) -> str:
        return self._name
    
    @property
    def tables(self) -> list[Table]:
        return self._tables
        
    def __str__(self):
        return f"Application ({self.name}) contains {len(self.tables)} tables: {', '.join([table.name for table in self.tables])}"
    