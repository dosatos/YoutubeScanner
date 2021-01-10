from pprint import pprint

from pydantic import PositiveInt

from app import ScanQuery, ScannerApp
from utils import rfs_3339_time
from utils.youtube import get_channel_id_by_video_id
from youtube_client import YoutubeClient


def get_videos(channel_id):
    query: ScanQuery = ScanQuery(
        channel_id=get_channel_id_by_video_id(
            YoutubeClient().api,
            channel_id),
        limit=PositiveInt(10),
        published_after=rfs_3339_time.week_ago()
    )
    scanner: ScannerApp = ScannerApp()
    pprint(scanner.get_videos(query=query))


def main():
    pass
    # client = YoutubeClient()
    # channel_id = get_channel_id_by_video_id(client.api, '1SD18klTuYk')
    # print(channel_id)

    get_videos(channel_id='1SD18klTuYk')


if __name__ == '__main__':
    main()
