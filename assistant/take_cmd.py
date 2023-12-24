import time
import speech_recognition as sr
import pygame
from threading import Thread

from modules.speech_module import talk
from settings.config import assistanceName
from settings.config import is_wake_up
from utils.utils import get_assets_file_path
from modules.print_response_module import print_user_command
from modules.print_response_module import print_response

last_command_time = time.time()
listener = sr.Recognizer()

# Initialize pygame
pygame.mixer.init()

# Load the sound file
beep_sound_path = get_assets_file_path("../assets/computer-processing-sound.wav")
beep_sound = pygame.mixer.Sound(beep_sound_path)

def play_beep():
    Thread(target=beep_sound.play).start()

def take_cmd(sleep_timeout):
    global is_wake_up, last_command_time
    cmd = ""
    status = "\n\nListening..."
    try:
        with sr.Microphone() as source:
            print("\r" + status, end="", flush=True)  # Print the initial status
            voice = listener.listen(source, phrase_time_limit=4)
            if voice:
                status = "_Processing..."
                print("\r" + status)  # Print the updated status

            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            print("------>>>>Cmd: " + cmd)

            if is_wake_up:
                play_beep()  # Play the beep sound when the assistant is active
                print_user_command(cmd);
                print("\rYou said:", cmd) if is_wake_up else print("\rNot for assistant")
                last_command_time = time.time()  # Update last command time
                print(assistanceName + " is active :) ")

            else:
                if assistanceName in cmd:
                    play_beep()  # Play the beep sound when the assistant is active
                    print_user_command(cmd);
                    is_wake_up = True
                else:
                    cmd = ""
                    print("Not for assistant")

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
