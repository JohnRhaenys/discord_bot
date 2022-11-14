import discord

from core import auth
from discord.ext import commands

from core.constants import BOT_PREFIX
from core.helpers.general_helpers import get_user_current_voice_channel, join_channel
from core.exceptions import UserNotInVoiceChannelException
from core.song import Song
from core.youtube_api import YouTubeAPI


intents = discord.Intents().all()
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)
youtube_api = YouTubeAPI()


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Escape from Brazil'))


@bot.command(aliases=['p'])
async def play(ctx, *args):
    author = ctx.message.author
    try:
        author_channel = get_user_current_voice_channel(bot, author)
    except UserNotInVoiceChannelException as e:
        embed = discord.Embed(description=e.message, color=0xFF0000)
        await ctx.send(embed=embed)
        return

    query = ' '.join(args)
    video = youtube_api.get_video(query)
    voice_client = await join_channel(author_channel)
    song = Song(video.title, video.url, ctx.author, voice_client)
    await song.play()


@bot.command()
async def magic(ctx):
    members = ctx.guild.members
    for member in members:
        print(member.name)


bot.run(auth.TOKEN)
