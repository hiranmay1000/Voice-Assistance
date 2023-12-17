import pyttsx3 as tt
import speech_recognition as sr
import pywhatkit
from datetime import datetime as dt

listener = sr.Recognizer()
engine = tt.init()

voices = engine.getProperty('voices')

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("Welcome boss! How can I help you")


def takeCmd():
    cmd = ""
    try:

        with sr.Microphone() as source:
            print("\n\nSay something...")
            listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            voice = listener.listen(source, timeout=6)  # Set a timeout to avoid blocking indefinitely
            cmd = listener.recognize_google(voice)  # Use recognize_sphinx instead of recognize_google
            cmd = cmd.lower()
            if 'alexa' in cmd: 
                cmd = cmd.replace('alexa', "")          
                print("You said: ", cmd)  

    except:
        pass

    return cmd



def run_alexa(cmd):

    if 'play' in cmd:
        song = cmd.replace("play", "")
        talk("Playing" + song + "on youtube")
        print("Alexa: Playing" + song)
        pywhatkit.playonyt(song)
        

while True:
    command = takeCmd()

    if 'shut down yourself' in command:
        talk("Shutting down")
        break
    else:
        run_alexa(command)


print("\n\n\nCode end...")
