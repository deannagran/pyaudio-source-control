import pyaudio,os
import speech_recognition as sr


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
            excel()
        elif user == "check":
            internet()
        elif user == "media":
            media()
    except:
        print("can't understand you bro")

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            print("listening...")
            mainfunction(source)
