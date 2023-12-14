from src.domain.post_action_listener import PostActionListener
from src.domain.task_response import TaskResponse
from src.infra.metadata_logger import MetaDataLogger


class PostAction:
    def __init__(self, log_metadata, metadata_service):
        self.metadataService = metadata_service
        self.listeners: list[PostActionListener] = []
        if log_metadata:
            self.listeners.append(MetaDataLogger())

    def perform(self, task_response: TaskResponse):
        metadata = self.metadataService.fetch(task_response)
        for listener in self.listeners:
            listener.listen(metadata)
