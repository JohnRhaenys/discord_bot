from time import sleep


VALID_COMMANDS = ('!my_songs',)


async def my_songs(message):
    await message.channel.send('Groovy, come here you scum! Fetch me these songs right now!!!')
    sleep(1)
    with open('songs.txt', 'r') as file:
        for song in file:
            await message.channel.send(f'-p {song}')
