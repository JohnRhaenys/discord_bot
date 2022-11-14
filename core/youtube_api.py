from googleapiclient.discovery import build

from core.youtube_video import YouTubeVideo

MAX_RESULTS = 1

# Your Youtube API key here
API_KEY = ''


class YouTubeAPI:
    def __init__(self):
        self.youtube = build('youtube', 'v3', developerKey=API_KEY, cache_discovery=False)

    def get_video(self, query, max_results=MAX_RESULTS):
        request = self.youtube.search().list(
            q=query, part='snippet', type='video', maxResults=max_results
        )

        response = request.execute()

        video = response['items'][0]
        video_title = video['snippet']['title']
        video_id = response['items'][0]['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        return YouTubeVideo(video_title, video_url)
