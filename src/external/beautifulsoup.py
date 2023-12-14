"""Module managing bs4 dependency"""
from bs4 import BeautifulSoup

from src.external.dto.parser_response import ParserResponse


class BeautifulSoupService:
    """Class Managing all interactions with bs4"""

    def parse(self, html_content: str) -> ParserResponse:
        """Function for extracting metadata information from html string"""
        soup = BeautifulSoup(html_content, "html.parser")
        links = soup.find_all("a")
        images = soup.find_all("img")
        return ParserResponse(links=links, images=images)
