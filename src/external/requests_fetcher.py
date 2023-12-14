import requests
import validators
from validators import ValidationError

from src.domain.fetch_response import FetchResponse
from src.domain.fetcher import Fetcher
from src.util.utils import InvalidEmailException, logger


class RequestsFetcher(Fetcher):
    def __init__(self):
        self.session = requests.Session()

    def fetch(self, url):
        try:
            self.validate(url)
            response = self.session.get(url, timeout=30)
            if response.ok:
                return FetchResponse(True, content=response.text)
            else:
                return FetchResponse(False, error=response.text)
        except InvalidEmailException as ice:
            logger.error("Invalid parameter: %s --> skipping", url)
            return FetchResponse(False, error=str(ice))
        except Exception as e:
            logger.error("Failed to fetch: %s, error: %s", url, str(e))
            return FetchResponse(False, error=str(e))

    def validate(self, url):
        result = validators.url(url)
        if isinstance(result, ValidationError):
            raise InvalidEmailException()
