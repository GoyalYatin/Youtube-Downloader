import moviepy.editor as mp

# Convert all the videos in folder to audio
clip = mp.VideoFileClip("../videos/")
clip.audio.write_audiofile("../songs/")

