from typing import List, Optional

from pydantic import (
    BaseModel,
    PositiveInt
)

from utils import rfs_3339_time
from youtube_client import YoutubeClient


class ScanQuery(BaseModel):
    channel_id: str
    limit: PositiveInt = 1
    published_after: str = rfs_3339_time.yesterday()


class ChannelPage:
    def __init__(self, response):
        self.response = response


class ChannelPageIterator:
    """
    Note:
        looks like there is no need to set the limits,
        YT anyways throttles requests based on daily quotas https://developers.google.com/youtube/v3/getting-started#calculating-quota-usage
    """

    YOUTUBE: YoutubeClient = YoutubeClient()

    def __init__(self, query: ScanQuery):
        self.query: ScanQuery = query
        self.video_count: PositiveInt = PositiveInt(0)

        self.last_response = None

    def __iter__(self):
        return self

    def __next__(self) -> ChannelPage:
        if self._exceeds_limit() or not self._has_next_page_token():
            raise StopIteration
        response = self.YOUTUBE.get_single_page(query=self.query,
                                                page_token=self._get_next_page_token())
        self._update_video_ids(response)
        self._update_last_response(response)
        return ChannelPage(self.last_response)

    def _update_video_ids(self, response):
        video_ids = self._get_video_ids(response)
        self.video_count += len(video_ids)

    def _get_video_ids(self, response) -> List[str]:
        page_limit = self.query.limit - self.video_count
        video_ids = [item['id']['videoId'] for item in response['items']][:page_limit]
        return video_ids

    def _exceeds_limit(self) -> bool:
        return self.query.limit is not None and self.video_count >= self.query.limit

    def _has_next_page_token(self) -> bool:
        if self.last_response is None:
            return True
        return self.last_response and self.last_response.get('nextPageToken')

    def _get_next_page_token(self) -> Optional[str]:
        return self.last_response.get('nextPageToken') if self.last_response else None

    def _update_last_response(self, response):
        """Used by self._has_next_page_token to check if the next page exists"""
        self.last_response = response


def get_videos(query: ScanQuery) -> List[str]:
    iterator: ChannelPageIterator = ChannelPageIterator(query=query)
    return _scan_channel(page_iterator=iterator)


def _scan_channel(page_iterator: ChannelPageIterator) -> List[str]:
    return [page.response for page in page_iterator]
