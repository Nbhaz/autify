import datetime
import unittest
from unittest.mock import MagicMock
from src.domain.task import Task
from src.domain.task_response import TaskResponse
from src.infra.post_action import PostAction
from src.infra.task_orchestrator import TaskOrchestrationService


class TestTaskOrchestrationService(unittest.TestCase):
    def setUp(self):
        self.mock_post_action = MagicMock(spec=PostAction)

    def test_perform_with_success(self):
        # Create an instance of TaskOrchestrationService
        task_orchestration_service = TaskOrchestrationService(
            post_action=self.mock_post_action
        )

        # Create a task and mock its execute method
        mock_task = MagicMock(spec=Task)
        mock_task_response = TaskResponse(
            success=True, key="test", execution_time=datetime.datetime.now()
        )
        mock_task.execute.return_value = mock_task_response

        # Add the task to the service
        task_orchestration_service.add_task(mock_task)

        # Call the perform method
        task_orchestration_service.perform()

        # Check that the task was executed and the postAction was called
        mock_task.execute.assert_called_once()
        self.mock_post_action.perform.assert_called_once_with(mock_task_response)

    def test_perform_with_failure(self):
        # Create an instance of TaskOrchestrationService
        task_orchestration_service = TaskOrchestrationService(
            post_action=self.mock_post_action
        )

        # Create a task and mock its execute method
        mock_task = MagicMock(spec=Task)
        mock_task_response = TaskResponse(
            success=False, key="test", execution_time=datetime.datetime.now()
        )
        mock_task.execute.return_value = mock_task_response

        # Add the task to the service
        task_orchestration_service.add_task(mock_task)

        # Call the perform method
        task_orchestration_service.perform()

        # Check that the task was executed, but the postAction was not called for a failed task
        mock_task.execute.assert_called_once()
        self.mock_post_action.perform.assert_not_called()
