from typing import Optional

from pydantic import BaseModel
from whale_client.api.entry import post_application
from whale_client.models.api.entry import PostApplicationRequest, PostApplicationResponse
from whale_client.models.application import Application
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class Manager(BaseModel):

    def commit(self, application: Application) -> Optional[str]:
        tables_dump: list[dict] = [table.model_dump() for table in application.tables]
        input = PostApplicationRequest(name=application.name, tables=tables_dump)
        response: Optional[PostApplicationResponse] = post_application(input=input)
        if not response:
            log.error("Failed to commit application.")
            return None
        return response.name
