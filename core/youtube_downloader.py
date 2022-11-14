import pafy


def download_mp3(url):
    video = pafy.new(url)
    audiostreams = video.audiostreams
    audiostreams[0].download()
