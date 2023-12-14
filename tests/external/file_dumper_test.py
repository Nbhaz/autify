import os
import unittest

import requests

from src.external.file_dumper import FileDumper


class FileDumperBaseTest(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.dumper = FileDumper()
        self.test_dir = 'test_files'
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Clean up: Remove the temporary directory and its contents
        for file_name in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, file_name)
            os.remove(file_path)
        os.rmdir(self.test_dir)


class FileSaveDumperTest(FileDumperBaseTest):

    def test(self):
        content = requests.get("https://www.google.com").text
        self.dumper.save(os.path.join(self.test_dir, "www.google.com.html"), content)
        self.assertTrue(os.path.isfile(os.path.join(self.test_dir, "www.google.com.html")))


class FileFetchDumperTest(FileDumperBaseTest):

    def test(self, file_name, content):
        content = requests.get("https://www.google.com").text
        with open(os.path.join(self.test_dir, "www.google.com.html"), "w") as file:
            file.write(content)
        content_fetched = self.dumper.fetch(os.path.join(self.test_dir, "www.google.com.html"))
        self.assertEquals(content_fetched, content)
