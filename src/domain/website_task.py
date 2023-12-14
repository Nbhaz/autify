from datetime import datetime
from urllib.parse import urlparse

from src.domain.dumper import Dumper
from src.domain.fetcher import Fetcher
from src.domain.task import Task
from src.domain.task_response import TaskResponse


class WebsiteTask(Task):
    def __init__(self, url: str, fetcher: Fetcher, dumper: Dumper = None):
        self.url = url
        self.fetcher = fetcher
        self.dumper = dumper

    def execute(self):
        fetch_response = self.fetcher.fetch(self.url)
        if fetch_response.is_success() and self.dumper:
            hostname = urlparse(self.url).hostname
            filename = f"{hostname}.html"
            self.dumper.save(key=filename, content=fetch_response.get_content())
            return TaskResponse(
                success=True, key=filename, execution_time=datetime.now()
            )
        return TaskResponse(success=False, key=None, execution_time=datetime.now())
