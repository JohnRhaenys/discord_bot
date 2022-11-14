from core.exceptions import UserNotInVoiceChannelException
from discord.ext import commands
import discord


def get_user_current_voice_channel(bot, user):
    voice_channels = get_voice_channels(bot)
    for voice_channel in voice_channels:
        members = voice_channel.members

        for m in members:
            if m.name == user.name:
                return voice_channel

    raise UserNotInVoiceChannelException


def get_channels(bot):
    return bot.get_all_channels()


def get_voice_channels(bot):
    return [channel for channel in get_channels(bot) if str(channel.type) == 'voice']


def get_text_channels(bot):
    return [channel for channel in get_channels(bot) if str(channel.type) == 'text']


async def join_channel(voice_channel):
    voice_client = await voice_channel.connect()
    return voice_client


async def leave_channel(voice_channel):
    await voice_channel.disconnect()
