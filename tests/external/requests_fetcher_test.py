import unittest

from src.external.requests_fetcher import RequestsFetcher
from src.util.constants import INVALID_URL


class RequestsFetcherBaseTest(unittest.TestCase):
    def setUp(self):
        self.fetcher = RequestsFetcher()


class ValidUrlFetchTest(RequestsFetcherBaseTest):
    def test(self):
        response = self.fetcher.fetch("https://www.morff.io")
        self.assertTrue(response.is_success())
        self.assertIsNotNone(response.get_content())
        self.assertIsNone(response.get_error())


class InValidUrlFetchTest(RequestsFetcherBaseTest):
    def test(self):
        response = self.fetcher.fetch("http/www.morff.io")
        self.assertFalse(response.is_success())
        self.assertIsNone(response.get_content())
        self.assertIsNotNone(response.get_error())
        self.assertEquals(response.get_error(), INVALID_URL)


class UrlFetchErrorTest(RequestsFetcherBaseTest):
    def test(self):
        response = self.fetcher.fetch("https://abc.xyz.tbc")
        self.assertFalse(response.is_success())
        self.assertIsNone(response.get_content())
        self.assertIsNotNone(response.get_error())
