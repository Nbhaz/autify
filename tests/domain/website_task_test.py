import datetime
import unittest
from unittest.mock import MagicMock
from src.domain.dumper import Dumper
from src.domain.fetcher import Fetcher
from src.domain.task_response import TaskResponse
from src.domain.website_task import WebsiteTask


class TestWebsiteTask(unittest.TestCase):
    def setUp(self):
        self.mock_fetcher = MagicMock(spec=Fetcher)
        self.mock_dumper = MagicMock(spec=Dumper)

    def test_execute_success_with_dumper(self):
        # Create an instance of WebsiteTask
        website_task = WebsiteTask(
            url="http://example.com", fetcher=self.mock_fetcher, dumper=self.mock_dumper
        )

        # Mock the fetcher response
        mock_fetch_response = MagicMock()
        mock_fetch_response.is_success.return_value = True
        mock_fetch_response.get_content.return_value = "Mocked HTML content"
        self.mock_fetcher.fetch.return_value = mock_fetch_response

        # Mock the dumper save method
        mock_dumper_save_response = TaskResponse(
            success=True, key="example.com.html", execution_time=datetime.datetime.now()
        )
        self.mock_dumper.save.return_value = mock_dumper_save_response

        # Call the execute method
        website_task.execute()

        # Assert that fetcher.fetch and dumper.save were called with the expected arguments
        self.mock_fetcher.fetch.assert_called_once_with("http://example.com")
        self.mock_dumper.save.assert_called_once_with(
            key="example.com.html", content="Mocked HTML content"
        )

    def test_execute_failure(self):
        # Create an instance of WebsiteTask
        website_task = WebsiteTask(
            url="http://example.com", fetcher=self.mock_fetcher, dumper=self.mock_dumper
        )

        # Mock the fetcher response
        mock_fetch_response = MagicMock()
        mock_fetch_response.is_success.return_value = False
        self.mock_fetcher.fetch.return_value = mock_fetch_response

        # Call the execute method
        result = website_task.execute()

        # Assert that fetcher.fetch was called with the expected argument
        self.mock_fetcher.fetch.assert_called_once_with("http://example.com")

        # Assert that the result is a failure TaskResponse
        self.assertIsInstance(result, TaskResponse)
        self.assertFalse(result.success)
