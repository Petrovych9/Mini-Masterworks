import pytube
# import pygame
import moviepy.editor

'''New feature: cut audio from video by link from YouTube '''


URL = 'https://www.youtube.com/watch?v=M_SMi5Tfq48'
folderForSave = 'D:\BOHDAN PETROVYCH\progr\project\BookManagementSystem\downloadedVideo'


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

# def playAudio(path):
#     pygame.init()
#     pygame.mixer_music.load(path)   #loat music
#     pygame.mixer_music.play()
#     userInput = 'c'
#     while userInput != 's':
#         userInput = input("Available commands: p-PAUSE, c-CONTINUE, s-STOP.")
#         if userInput == 'p':
#             pygame.mixer_music.pause()
#         elif userInput == 'c':
#             pygame.mixer_music.unpause()
#         elif userInput == 's':
#             pygame.mixer_music.stop()
#             print("Have a great day!!!")
#             break
#
#     pygame.quit()

