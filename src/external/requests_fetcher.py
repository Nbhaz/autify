from validators import ValidationError

from src.domain.fetch_response import FetchResponse
from src.domain.fetcher import Fetcher
import requests
import validators

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
            logger.error(f"Invalid parameter: {url} --> skipping")
            return FetchResponse(False, error=str(ice))
        except Exception as e:
            logger.error(f"Failed to fetch: {url}, error: {str(e)}")
            return FetchResponse(False, error=str(e))

    def validate(self, url):
        result = validators.url(url)
        if isinstance(result, ValidationError):
            raise InvalidEmailException()

