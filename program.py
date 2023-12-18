import pyttsx3 as tt
import speech_recognition as sr
import pywhatkit
import wikipedia as wiki
import random
import pyjokes as jokes
from datetime import datetime as dt
from time import sleep



assistanceName = "servo"

listener = sr.Recognizer()
engine = tt.init()

# Get all available voices
voices = engine.getProperty('voices')

# Select a female voice
female_voice = [voice for voice in voices if 'female' in voice.name.lower()]

if female_voice:
    engine.setProperty('voice', female_voice[0].id)
else:
    print("No female voice found. Using the default voice.")

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("Welcome boss")


def print_response(cmd):
    print(assistanceName + ':', end = ' ')
    for word in cmd:
        print(''.join(char for char in word), end='', flush=True)
        sleep(0.025)


def play_music(song):
    words_to_remove = ["can", "play", "you"]
    
    for word in words_to_remove:
        song = song.replace(word, "")

    song = song.replace("play", "")
    pywhatkit.playonyt(song)
    talk("Playing" + song + "on youtube")
    mess = 'Playing' + song
    print_response(mess)

def search_wiki(cmd):
    words_to_remove = ["who", "is", "the", "heck", "hell", "mr", "mrs", "ms"]
    
    for word in words_to_remove:
        cmd = cmd.replace(word, "")

    try:
        output = wiki.summary(cmd, sentences=4)
        talk("Here are some results")
        print_response(output)
    except Exception as e:
        talk(str(e))
        print_response((str(e)))


def process_time():
    formatted_time = dt.now().strftime("%I:%M %p")
    print_response(formatted_time)
    talk(formatted_time)

def process_date():
    formatted_date = dt.now().strftime("%d %B %Y")
    print_response(formatted_date)
    talk(formatted_date)

def process_name_req():
    mess = ["No doubt about it", "Definately I like my name" + assistanceName, "Yes I got a very cool name", "Yes I like it", "I like my name very much"]

    selected_mess = random.choice(mess)
    print_response(selected_mess)
    talk(selected_mess)

def get_boss_info():
    mess = "My boss is Mr Hiranmay, and he assigned me this name"
    talk(mess)
    print(mess)

def process_joke():
    joke = jokes.get_joke()
    talk(joke)
    print_response(joke)

def failed_cmd_inp():
    messages = [
        "Sorry I couldn't hear you properly!",
        "Can you say that again?",
        "I am really sorry I don't get it.",
        "I am not sure what you are saying."
    ]

    selected_message = random.choice(messages)
    print_response(selected_message)
    talk(selected_message)



def take_cmd():
    cmd = ""
    try:
        with sr.Microphone() as source:
            print("\n\nListening...")
            listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            voice = listener.listen(source, timeout=60)  # Set a timeout to avoid blocking indefinitely
            cmd = listener.recognize_google(voice) 
            cmd = cmd.lower()
            if assistanceName in cmd: 
                cmd = cmd.replace(assistanceName, "")          
                print("You said:", cmd)
            else:
                print("Did you said to me?")
                return "Did you said to me?"


    except sr.UnknownValueError:
        mess = "Google Speech Recognition could not understand audio and is up for command."
        return mess
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    return cmd




def run_alexa(cmd):

    if any(keyword in cmd for keyword in ['what time is it', 'what is the time', 'what is the time now', 'tell me the time', 'time now', 'the time']):
        process_time()
    elif any(keyword in cmd for keyword in [ 'what date is it', 'what date today', 'what is the date today', "today's date", 'tell me the date', 'date today', "the date"]):
        process_date()
    elif any(keyword in cmd for keyword in ['do you like your name', 'how much like your name', 'is your name cool']):
        process_name_req()
    elif any(keyword in cmd for keyword in ['who gave your name', 'who assign your name', 'who is your boss']):
        get_boss_info()
    elif 'your name' in cmd:
        talk('My name is ' + assistanceName)
    elif "Google Speech Recognition could not understand audio and is up for command." in cmd:
        print(assistanceName + " is listening...")
    elif 'joke' in cmd:
        process_joke()
    elif 'play' in cmd:
        play_music(cmd)
    elif 'who' in cmd:
        search_wiki(cmd)
    else:
        talk("Sorry I don't have that information as of now")



    
    
        
        

while True:
    command = take_cmd()

    if 'shut down yourself' in command:
        talk("Shutting down")
        print_response("Processing request...\nShutting down...")
        break
    else:
        run_alexa(command)


print("\n\nEnd of code...")




# export DISPLAY=:0
# xhost +SI:localuser:your_username

