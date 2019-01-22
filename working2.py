import pyaudio,os
import speech_recognition as sr
from subprocess import call
import socket   #for sockets
import sys  #for exit


try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();

print 'Socket Created'

host = '10.247.75.32' #Crestron Processor IP
port = 5005 #The port specified in Simpl programs TCP/IP Server symbol

try:
    remote_ip = socket.gethostbyname( host )

except socket.gaierror:
    #Could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

print 'Ip address of ' + host + ' is ' + remote_ip

#Connect to remote server
s.connect((remote_ip , port))

call(['espeak', 'SOCKET CONNECTED.'])
print 'Socket Connected to ' + host + ' on ip ' + remote_ip


def mainfunction(source):
    audio = r.listen(source)

    try:
        user = r.recognize_google(audio, language = "en-us", show_all=False)
        user = user.lower()
        print(user)
        #EVENT AREA COMMANDS-----------------------------------------
        
        if user == "event area projector on":
            call(['espeak', 'TURNING ON EVENT AREA PROJECTOR..'])
            s.send('event area projector on')
        elif user == "turn off lights in event area":
            call(['espeak', 'TURNING OFF LIGHTS IN EVENT AREA...'])
            s.send('event area lights off')
            
        #LOBBY COMMANDS-----------------------------------------------

        elif user == "lobby monitor on":
            call(['espeak', 'TURNING ON LOBBY MONITOR...'])
            s.send('lobby monitor on')
        elif user == "lobby monitor off":
            call(['espeak', 'TURNING OFF LOBBY MONITOR...'])
            s.send('lobby monitor off')
        elif user == "turn off lights in lobby":
            call(['espeak', 'TURNING OFF LOBBY LIGHTS...'])
            s.send('lobby lights off')
            
        #INVALID COMMAND-----------------------------------------------
        else:
            call(['espeak', 'NOT A VALID VOICE COMMAND. TRY AGAIN.'])
            print("Not a valid voice command. Try again.")
    except:
        #UNRECOGNIZABLE COMMAND-----------------------------------------
        print("Cannot understand you. Please repeat your command.")
        call(['espeak', 'CANNOT UNDERSTAND YOU. PLEASE REPEAT YOUR COMMAND...'])

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            print "Listening..."
            mainfunction(source)
