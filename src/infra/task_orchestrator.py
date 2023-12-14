from src.domain.task import Task
from src.infra.post_action import PostAction


class TaskOrchestrationService:
    def __init__(self, post_action: PostAction, tasks: list[Task] = None):
        self._taskQueue = tasks if tasks else []
        self.postAction = post_action

    def add_task(self, task):
        self._taskQueue.append(task)

    def add_tasks(self, tasks):
        self._taskQueue.extend(tasks)

    def perform(self):
        while self._taskQueue:
            task = self._taskQueue.pop(0)
            taskResponse = task.execute()
            if taskResponse.is_success() and self.postAction:
                self.postAction.perform(taskResponse)
