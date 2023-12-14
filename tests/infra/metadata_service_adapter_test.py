import unittest
from datetime import datetime
from unittest.mock import patch
from src.domain.metadata import Metadata
from src.domain.task_response import TaskResponse
from src.infra.metadata_service_adapter import MetaDataServiceAdapter


class TestMetaDataServiceAdapter(unittest.TestCase):
    @patch("src.domain.dumper.Dumper")
    def test_fetch_returns_metadata(self, mock_dumper_class):
        # Mocking the Dumper
        mock_dumper = mock_dumper_class.return_value

        # Setting up mock data
        key = "example_key"
        html_data = '<html><body><a href="link1">Link 1</a></body></html>'
        execution_time = datetime(2023, 10, 31, 12, 34, 56)

        # Mocking the fetch method of Dumper
        mock_dumper.fetch.return_value = html_data

        # Creating an instance of MetaDataServiceAdapter
        meta_data_service_adapter = MetaDataServiceAdapter(mock_dumper)

        # Creating a TaskResponse
        task_response = TaskResponse(True, key=key, execution_time=execution_time)

        # Calling the fetch method
        result = meta_data_service_adapter.fetch(task_response)

        # Asserting that the fetch method of Dumper was called with the correct key
        mock_dumper.fetch.assert_called_once_with(key)

        # Asserting that the result is an instance of Metadata with the expected values
        self.assertIsInstance(result, Metadata)
        self.assertEqual(result.filename, key)
        self.assertEqual(result.links[0].text, "Link 1")
        self.assertEqual(result.images, [])
        self.assertEqual(result.lastFetch, execution_time)
