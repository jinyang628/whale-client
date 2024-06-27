from whale.models.table import Table

VERSION = "v1"

# TODO: Use pydantic BaseModel
class Application:
    
    tables: list[Table]
    
    def __init__(self, tables: list[Table]):
        table_names = [table.name for table in tables]
        if len(table_names) != len(set(table_names)):
            raise ValueError("Table names passed into ApiManager are not unique.")
        self.tables = tables
        
    def __str__(self):
        return f"ApiManager with {len(self.tables)} tables: {', '.join([table.name for table in self.tables])}"