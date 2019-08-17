from pytube import YouTube
from pytube import Playlist

# download a video
YouTube('https://www.youtube.com/watch?v=hGXf0FsW0A4').streams\
        .first()\
        .download(output_path="../videos")

# download with filters
YouTube('https://www.youtube.com/watch?v=wYhjXLbNmho').streams\
        .filter(subtype='mp4')\
        .first()\
        .download(output_path='../videos')


# downloading a playlist
pl = Playlist("https://www.youtube.com/playlist?list=PLGVShb98UkHiaI0nkyv4EfoP5InL2qVdv")
pl.download_all('../videos')