import moviepy.editor as mp
import speech_recognition as sr

# Load the video
video = mp.VideoFileClip("[eground.org] 038 Decorating functions with parameters.mp4")

# Extract the audio from the video
audio_file = video.audio
audio_file.write_audiofile("Decorating.wav")

r = sr.Recognizer()

with sr.AudioFile("Decorating.wav") as source:
    data = r.record(source)

text = r.recognize_google(data)

print("\nThe resultant text from video is: \n")
print(text)
