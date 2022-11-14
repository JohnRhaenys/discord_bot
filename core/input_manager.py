from core import responses, my_commands
from core.auth import ALLOWED_AUTHORS


def is_valid_author(author_name):
    return author_name in ALLOWED_AUTHORS


async def get_response(client, message):

    message_str = str(message.content)
    author_name = str(message.author)

    if not message_str.strip():
        return None

    if not is_valid_author(author_name):
        return responses.CANNOT_TALK

    await my_commands.my_songs(message)
