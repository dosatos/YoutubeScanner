from typing import Optional


def get_channel_id_by_video_id(service, video_id: str) -> Optional[str]:
    if video_id is None:
        raise ValueError("video_id was not provided")
    request = service.videos().list(part='snippet', id=video_id)
    response = request.execute()
    if 'items' not in response:
        return None
    channel_id = response['items'][0]['snippet']['channelId']
    return channel_id
