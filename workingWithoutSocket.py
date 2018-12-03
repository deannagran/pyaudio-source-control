import pyaudio,os
import speech_recognition as sr
from subprocess import call
import socket   #for sockets
import sys  #for exit


f=open('voicecommands.txt')
lines=f.readlines()
print "AVAILABLE VOICE COMMANDS......"
print "Event Area:"
print "1. " + lines[0] + "2. " + lines[1] + "3. " + lines[2] + "4. " + lines[3] + "5. " + lines[4] + "6. " + lines[5] + "7. " + lines[6]
print "Lobby:"
print "8. " + lines[7] + "9. " + lines[8] + "10. " + lines[9] 

def mainfunction(source):
    audio = r.listen(source)


    try:
        user = r.recognize_google(audio, language = "en-us", show_all=False)
        user = user.lower()
        print(user)
        #EVENT AREA COMMANDS-----------------------------------------
        
        if user == lines[0]:
            call(['espeak', 'TURNING ON EVENT AREA PROJECTOR..'])
            s.send('event area projector on')
        elif user == lines[1]:
            call(['espeak', 'TURNING OFF PROJECTOR IN EVENT AREA...'])
            s.send('event area projector off')
        elif user == lines[2]:
            call(['espeak', 'MUTING AUDIO IN EVENT AREA...'])
            s.send('mute event area audio')
        elif user == lines[3]:
            call(['espeak', 'UNMUTING EVENT AREA...'])
            s.send('unmute event area audio')
        elif user == lines[4]:
            call(['espeak', 'RAISING MICROPHONE VOLUME...'])
            s.send('raise mic volume')
        elif user == lines[5]:
            call(['espeak', 'LOWERING MICROPHONE VOLUME...'])
            s.send('lower mic volume')
        elif user == lines[6]:
            call(['espeak', 'DISPLAY SIGNAGE ON EVENT MONITOR...'])
            s.send('show event signage')
        #LOBBY COMMANDS-----------------------------------------------

        elif user == lines[7]:
            call(['espeak', 'TURNING ON LOBBY MONITOR...'])
            s.send('lobby monitor on')
        elif user == lines[8]:
            call(['espeak', 'TURNING OFF LOBBY MONITOR...'])
            s.send('lobby monitor off')
        elif user == lines[9]:
            call(['espeak', 'DISPLAYING SIGNAGE ON LOBBY MONITOR...'])
            s.send('show lobby signage')
            
        #INVALID COMMAND-----------------------------------------------
        else:
            print("Invalid voice command. Please try again.")
            call(['espeak', 'NOT A VALID VOICE COMMAND. TRY AGAIN.'])
    except:
        #UNRECOGNIZABLE COMMAND-----------------------------------------
        print("Cannot understand you. Please repeat your command.")
        call(['espeak', 'CANNOT UNDERSTAND YOU. PLEASE REPEAT YOUR COMMAND...'])

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            print("listening...")
            mainfunction(source)
