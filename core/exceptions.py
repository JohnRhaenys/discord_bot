class UserNotInVoiceChannelException(Exception):
    def __init__(self):
        self.message = 'You have to be connected to a voice channel before you can use this command!'
