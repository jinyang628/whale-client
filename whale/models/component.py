from pydantic import BaseModel

from whale.models.database.api_manager import ApiManager

class Component(BaseModel):
    name: str
    description: str
    api_manager: ApiManager
    
    def __init__(self, name: str, description: str, api_manager: ApiManager):
        self.name = name
        self.description = description
        self.api_manager = api_manager

    def __str__(self):
        return f"{self.name} ({self.description})"
    
    