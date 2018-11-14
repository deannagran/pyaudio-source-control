import pyaudio
from subprocess import call
import speech_recognition as sr;

r = sr.Recognizer()
with sr.Microphone(device_index = 2) as source:
    audio = r.listen(source)

try:
    print("Speech was:" + r.recognize_google(audio, language = "en-us", show_all=False))
except LookupError:
    print("Could not understand audio...")
