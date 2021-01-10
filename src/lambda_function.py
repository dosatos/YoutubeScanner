import json
import logging

from pydantic import PositiveInt

from app import ScanQuery, ScannerApp
from utils import rfs_3339_time


def lambda_handler(event, context):
    try:
        channel_id: str = event['channel_id']
    except KeyError:
        return client_failure()

    try:
        query: ScanQuery = ScanQuery(
            channel_id=channel_id,
            limit=PositiveInt(10),
            published_after=rfs_3339_time.week_ago()
        )
        scanner: ScannerApp = ScannerApp()
        results = scanner.get_videos(query=query)
    except Exception as e:
        return server_failure(event, e)
    return success(results)


def client_failure(event):
    message = f"no `channel_id` found in the request. event: {event}"
    logging.error(message)
    return {
        "statusCode": 400,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {"results": message}
    }


def server_failure(channel_id: str, exception):
    message: str = f"could not have processed for channel_id: {channel_id}. Trace: {exception.value}"
    logging.error(message)
    return {
        "statusCode": 500,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {"results": message}
    }


def success(results):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {
            "results": json.dumps(results)
        }
    }
