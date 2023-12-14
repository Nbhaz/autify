""" Main module invoking all the functions"""
import argparse

from src.domain.website_task import WebsiteTask
from src.external.file_dumper import FileDumper
from src.external.requests_fetcher import RequestsFetcher
from src.infra.post_action import PostAction
from src.infra.task_orchestrator import TaskOrchestrationService
from src.infra.metadata_service_adapter import MetaDataServiceAdapter


def main():
    parser = argparse.ArgumentParser(
        description="Fetch web pages and save them to disk for later retrieval and browsing."
    )
    parser.add_argument("urls", nargs="+", help="URLs to fetch")
    parser.add_argument(
        "--metadata",
        action="store_true",
        help="Include metadata and create a local mirror",
    )
    args = parser.parse_args()
    fetcher = RequestsFetcher()
    dumper = FileDumper()
    metadata_service = MetaDataServiceAdapter(dumper=dumper)
    tasks = [WebsiteTask(url=url, fetcher=fetcher, dumper=dumper) for url in args.urls]
    post_action = PostAction(
        log_metadata=args.metadata, metadata_service=metadata_service
    )
    tasks_orchestration = TaskOrchestrationService(post_action=post_action, tasks=tasks)
    tasks_orchestration.perform()


if __name__ == "__main__":
    main()
