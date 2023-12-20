import pyttsx3 as tt
import speech_recognition as sr
import pywhatkit
import wikipedia as wiki
import random
import pyjokes as jokes
import time

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
    talk( "Its" + formatted_date)

def process_name_req():
    mess = ["No doubt about it", "Definately I like my name " + assistanceName, "Yes I got a very cool name", "Yes I like it", "I like my name very much"]

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
    elif 'joke' in cmd:
        process_joke()
    elif 'play' in cmd:
        play_music(cmd)
    elif 'who' in cmd:
        search_wiki(cmd)
    elif cmd != "":
        talk("Sorry I don't have that information as of now")


is_wake_up = True
last_command_time = time.time()

def take_cmd(sleep_timeout):
    global is_wake_up, last_command_time
    cmd = ""
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, phrase_time_limit=15)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            print("------>>>>Cmd: " + cmd)

            if is_wake_up:
                print("You said:", cmd)
                last_command_time = time.time()  # Update last command time
                print(assistanceName + " is active :) ")

            else:

                if assistanceName in cmd:
                    is_wake_up = True
                else:
                    cmd = ""
                    print("Not for assistant")
                    
                print(assistanceName + ": Did you say something?")
            
            cmd = cmd.replace(assistanceName, "")

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        is_wake_up = False
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")
    except sr.WaitTimeoutError:
        print("Listening timed out. Please try again.")
        is_wake_up = False

    # Check if it's time to go to sleep
    if not is_wake_up and time.time() - last_command_time > sleep_timeout:
        print(assistanceName + " is in sleep mode - zzz zz zzz")
        is_wake_up = False

    return cmd




while True:
    print("\n\n\nWhile loop------------")
    command = take_cmd(5)  # Adjust the sleep timeout as needed

    if any(keyword in command for keyword in ['shut down yourself', 'shutdown yourself', 'shut yourself', 'power off yourself']):
        talk("Shutting down")
        print("Processing request...\nShutting down...")
        break
    elif is_wake_up:
        run_alexa(command)

print("\n\nEnd of code...")




