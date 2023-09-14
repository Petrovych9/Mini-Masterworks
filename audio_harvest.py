import pytube
import moviepy.editor

'''New feature: cut audio from video by link from YouTube '''


URL = 'https://www.youtube.com/watch?v=M_SMi5Tfq48'
folderForSave = 'downloadedVideo'


def downloadVideo(url):
    yt = pytube.YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download(output_path=folderForSave)
    videoFilePath = folderForSave + "/" + video.default_filename
    return videoFilePath, video.default_filename

def extractAudio(url):
    path, name = downloadVideo(url)
    video = moviepy.editor.VideoFileClip(path)
    audio = video.audio
    audioPath = folderForSave+"/AUDIO_" + name + ".mp3"  # Specify the output audio file path
    audio.write_audiofile(audioPath)
    video.close()
    audio.close()
    return audioPath


