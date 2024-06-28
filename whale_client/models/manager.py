from typing import Optional

from pydantic import BaseModel
from whale_client.api.entry import post_entry
from whale_client.models.api.entry import EntryRequest, EntryResponse
from whale_client.models.application import Application
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class Manager(BaseModel):
    
    def commit(self, application: Application) -> Optional[str]:
        tables_dump: list[dict] = [table.model_dump() for table in application.tables]
        
        response: Optional[EntryResponse] = post_entry(
            input=EntryRequest(application=tables_dump)
        )
        if not response:
            log.error("Failed to commit application.")
            return None
        return response.id