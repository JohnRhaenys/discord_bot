from collections import deque


class Playlist:
    def __init__(self):
        self.queue = deque()
        self.current_song = self.queue.popleft()

    def queue(self, song):
        self.queue.append(song)

    def get_next(self):
        return self.queue.popleft()
