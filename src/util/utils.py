import logging

from src.util.constants import INVALID_URL


class InvalidEmailException(Exception):

    def __init__(self):
        super().__init__(INVALID_URL)


# Configure the logger
logging.basicConfig(
    level=logging.INFO,  # Set the logging level (e.g., INFO, DEBUG)
    format='%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Create a logger
logger = logging.getLogger(__name__)
