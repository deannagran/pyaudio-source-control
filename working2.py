import pyaudio,os
import speech_recognition as sr
from subprocess import call

call(['espeak', 'HELLO TREY. PLEASE ALLOW TWENTY TO THIRTY SECONDS FOR ME TO WARM UP....'])

def excel():
        #os.system("start excel.exe")
        print("start something excel")

def internet():
        #os.system("start chrome.exe")
        print("start something chrome")

def media():
        #os.system("start wmplayer.exe")
        print("start something media")

def mainfunction(source):
    audio = r.listen(source)

    try:
        user = r.recognize_google(audio, language = "en-us", show_all=False)
        print(user)
        if user == "Excel":
            call(['espeak', 'OPENING EXCEL..'])
            excel()
        elif user == "check":
            call(['espeak', 'PERFORMING CHECK..'])
            internet()
        elif user == "media":
            call(['espeak', 'OPENING MEDIA NOW...'])
            media()
    except:
        print("Cannot understand you. Please repeat your command.")
        call(['espeak', 'CANNOT UNDERSTAND YOU. PLEASE REPEAT YOUR COMMAND...'])

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            print("listening...")
            mainfunction(source)
