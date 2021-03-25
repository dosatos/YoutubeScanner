from pydantic import PositiveInt

import youtubescanner.scanner


def test_main():
    query: scanner.ScanQuery = scanner.ScanQuery(
        channel_id='UCkQX1tChV7Z7l1LFF4L9j_g',
        limit=PositiveInt(10)
    )
    assert 'items' in scanner.get_videos(query=query)[0]
