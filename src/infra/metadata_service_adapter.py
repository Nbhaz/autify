from src.domain.metadata import Metadata
from src.domain.metadata_service import MetadataService
from src.domain.task_response import TaskResponse
from src.external.beautifulsoup import BeautifulSoupService


class MetaDataServiceAdapter(MetadataService):
    def __init__(self, dumper):
        self.dumper = dumper
        self.parser = BeautifulSoupService()

    def fetch(self, task_response: TaskResponse) -> Metadata:
        html_data = self.dumper.fetch(task_response.key)
        parser_response = self.parser.parse(html_data)
        return Metadata(
            filename=task_response.key,
            links=parser_response.links,
            images=parser_response.images,
            last_fetch=task_response.executionTime,
        )
