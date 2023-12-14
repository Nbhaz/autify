import unittest
from datetime import datetime
from unittest.mock import patch
from src.domain.metadata import Metadata
from src.infra.metadata_logger import MetaDataLogger


class TestMetaDataLogger(unittest.TestCase):
    @patch("src.util.utils.logger.info")
    def test_listen_logs_metadata(self, mock_logger_info):
        # Create a Metadata object for testing
        metadata = Metadata(
            filename="example.com.html",
            links=["link1", "link2"],
            images=["image1.jpg", "image2.jpg"],
            last_fetch=datetime(2023, 10, 31, 12, 34, 56),
        )

        # Instantiate the MetaDataLogger
        meta_data_logger = MetaDataLogger()

        # Call the listen method
        meta_data_logger.listen(metadata)

        # Assert that the logger.info method was called with the expected log messages
        # Assert
        expected_log_message = (
            "site: example.com\n"
            "num_links: 2\n"
            "images: 2\n"
            "last_fetch: Tue Oct 31 2023 12:34:56 UTC"
        )
        mock_logger_info.assert_called_once_with(expected_log_message)
