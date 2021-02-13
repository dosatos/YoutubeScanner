from pprint import pprint

from pydantic import PositiveInt

from youtubescanner import scanner
from youtubescanner.utils import rfs_3339_time
from youtubescanner.utils.youtube import get_channel_id_by_video_id
from youtubescanner.youtube_client import YoutubeClient


def get_videos(channel_id):
    query: scanner.ScanQuery = scanner.ScanQuery(
        channel_id=get_channel_id_by_video_id(
            YoutubeClient().api,
            channel_id),
        limit=PositiveInt(10),
        published_after=rfs_3339_time.week_ago()
    )
    pprint(scanner.get_videos(query=query))


def main():
    pass
    # client = YoutubeClient()
    # channel_id = get_channel_id_by_video_id(client.api, '1SD18klTuYk')
    # print(channel_id)

    get_videos(channel_id='1SD18klTuYk')


if __name__ == '__main__':
    main()
