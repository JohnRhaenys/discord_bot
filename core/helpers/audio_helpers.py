from pafy import new
import discord

from core.constants import YDL_OPTIONS, FFMPEG_OPTIONS


async def play_audio(voice_client, url):
    if voice_client.is_playing():
        # Add song to playlist
        return

    ffmpeg_opts = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    video = new(url)
    audio = video.getbestaudio().url
    voice_client.play(discord.FFmpegPCMAudio(audio, **ffmpeg_opts))
    voice_client.is_playing()


async def test(voice_client, video_url):
    from discord import FFmpegPCMAudio
    from youtube_dl import YoutubeDL

    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(video_url, download=False)
    url = info['formats'][0]['url']
    voice_client.play(FFmpegPCMAudio(url, **FFMPEG_OPTIONS))
    voice_client.is_playing()
