from pydantic import PositiveInt

from app import ScannerApp, ScanQuery


def get_channel_id(url):
    return url


def test_main():
    query: ScanQuery = ScanQuery(channel_id=get_channel_id('UCkQX1tChV7Z7l1LFF4L9j_g'), limit=PositiveInt(10))
    scanner: ScannerApp = ScannerApp()
    assert scanner.get_videos(query=query) == ['https://www.google.com/playlist']
