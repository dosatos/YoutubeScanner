import os

from googleapiclient.discovery import (
    build,
)
from googleapiclient.errors import HttpError

from settings import LOGGER


class YoutubeClient:
    def __init__(self):
        self.api = build("youtube", "v3", developerKey=os.getenv("google_api_key"))

    def get_single_page(self, query, page_token):
        request = self.api.search().list(
            part='snippet,id',
            channelId=query.channel_id,
            type='video',
            pageToken=page_token,
            publishedAfter=query.published_after,
            maxResults=50
        )
        try:
            response = request.execute()
        except HttpError as e:
            LOGGER.error(f"Invalid channel.: {e}")
            raise e
        return response
