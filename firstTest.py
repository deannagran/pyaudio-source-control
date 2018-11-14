import pyaudio
from subprocess import call
import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold=4000
with sr.Microphone(device_index = 2, sample_rate = 44100, chunk_size = 512) as source:
    print 'LISTENING NOW...'
    audio = r.listen(source)
    print 'PROCESSING...'

    try:
        message = r.recognize_google(audio, language = 'en-us', show_all = False)
        call(["espeak", message])
    except:
        call(['espeak', 'CANNOT UNDERSTAND YOU...'])
