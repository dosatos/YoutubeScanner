from pydantic import PositiveInt

from app import ScannerApp, ScanQuery


def get_channel_id(url):
    return url


def test_main():
    query: ScanQuery = ScanQuery(channel_id=get_channel_id('UC6TWZR9vX5SCRCvu2anvYLQ'), limit=PositiveInt(10))
    scanner: ScannerApp = ScannerApp()
    assert scanner.scan(query=query) == ['https://www.google.com/playlist']
