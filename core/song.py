import discord

from core.helpers.audio_helpers import play_audio


class Song:
    def __init__(self, title, correspondent_video_url, requester, voice_client):
        self.title = title
        self.correspondent_video_url = correspondent_video_url
        self.requester = requester
        self.voice_client = voice_client

    def create_embed(self):
        if self.voice_client.is_playing():
            title = 'Added to queue',
            description = f'Queued [{self.title}]({self.correspondent_video_url}) [{self.requester.mention}]'
        else:
            title = f'Now playing',
            description = f'[{self.title}]({self.correspondent_video_url}) [{self.requester.mention}]'
        return discord.Embed(title=title, description=description, color=0x202225)

    async def play(self):
        await play_audio(self.voice_client, self.correspondent_video_url)
