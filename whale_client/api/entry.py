import json
from typing import Optional
import requests
from dotenv import load_dotenv

import os

import logging

from whale_client.models.api.entry import EntryRequest, EntryResponse

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


load_dotenv()
BASE_URL = os.getenv("BACKEND_ENDPOINT")
SERVICE_ENDPOINT = "entry"


def post_entry(input: EntryRequest) -> Optional[EntryResponse]:
    try:
        response = requests.post(
            f"{BASE_URL}/{SERVICE_ENDPOINT}", json=input.model_dump()
        )
        response.raise_for_status()
        entry_response = EntryResponse.model_validate(json.loads(response.text))
        return entry_response
    except TypeError as e:
        log.error(
            f"Failed to parse the response id of application from server: {e}"
        )
        return None
    except requests.RequestException as e:
        log.error(f"Failed to fetch response for application: {e}")
        return None
    except Exception as e:
        log.error(f"Unknown error for posting of application occurred: {e}")
        return None
