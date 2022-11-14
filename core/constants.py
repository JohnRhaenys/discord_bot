BOT_PREFIX = '.'

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}

FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

