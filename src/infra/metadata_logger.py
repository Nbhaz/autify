import os

from src.domain.metadata import Metadata
from src.domain.post_action_listener import PostActionListener
from src.util.utils import logger


class MetaDataLogger(PostActionListener):
    def listen(self, metadata: Metadata):
        filename_without_extension, _ = os.path.splitext(metadata.filename)
        log_message = (
            f"site: {filename_without_extension}\n"
            f"num_links: {len(metadata.links)}\n"
            f"images: {len(metadata.images)}\n"
            f"last_fetch: {metadata.lastFetch.strftime('%a %b %d %Y %H:%M:%S UTC')}"
        )
        logger.info(log_message)
        # logger.info(f"site: {filename_without_extension}")
        # logger.info(f"num_links: {len(metadata.links)}")
        # logger.info(f"images: {len(metadata.images)}")
        # logger.info(
        #     f"last_fetch: {metadata.lastFetch.strftime('%a %b %d %Y %H:%M:%S UTC')}"
        # )
