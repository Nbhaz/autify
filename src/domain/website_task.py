from src.domain.dumper import Dumper
from src.domain.fetcher import Fetcher
from src.domain.task import Task
from urllib.parse import urlparse

from src.domain.task_response import TaskResponse
from datetime import datetime


class WebsiteTask(Task):

    def __init__(self, url: str, fetcher: Fetcher, dumper: Dumper = None):
        self.url = url
        self.fetcher = fetcher
        self.dumper = dumper

    def execute(self):
        fetchResponse = self.fetcher.fetch(self.url)
        if fetchResponse.is_success() and self.dumper:
            hostname = urlparse(self.url).hostname
            filename = f"{hostname}.html"
            self.dumper.save(key=filename, content=fetchResponse.get_content())
            return TaskResponse(success=True, key=filename, executionTime=datetime.now())
        return TaskResponse(success=False, key=None, executionTime=datetime.now())
