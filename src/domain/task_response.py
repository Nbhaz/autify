from datetime import datetime


class TaskResponse:

    def __init__(self, success: bool, key: str, executionTime: datetime):
        self.key = key
        self.success = success
        self.executionTime = executionTime

    def is_success(self) -> bool:
        return self.success

    def get_key(self) -> str:
        return self.key
