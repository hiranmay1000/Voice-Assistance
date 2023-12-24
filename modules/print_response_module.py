import pygame

from threading import Thread
from utils.utils import get_log_file_path
from settings.config import assistanceName
from time import sleep
from utils.utils import get_assets_file_path
from settings.config import user


# Initialize pygame
pygame.mixer.init()

# Load the background music
background_music_path = get_assets_file_path("../assets/keyboard-typing-45s.wav")  # Replace with the path to your music file
pygame.mixer.music.load(background_music_path)

def play_keyboard_music():
    pygame.mixer.music.play()

def stop_background_music():
    pygame.mixer.music.stop()


#* user commands
#* user commands
def print_user_command(cmd):
    log_file_path = get_log_file_path()

    with open(log_file_path, 'a') as log_file:
        log_file.write(f'{user}: ')
        log_file.write(cmd)
        log_file.write("\n")  # Move this line inside the 'with' block


#* assistant commands
def print_response(cmd):
    log_file_path = get_log_file_path()

    # Start playing background music in a separate thread
    music_thread = Thread(target=play_keyboard_music)
    music_thread.start()

    with open(log_file_path, 'a') as log_file:
        log_file.write(f'{assistanceName}: ')
        for word in cmd:
            print(''.join(char for char in word), end='', flush=True)
            sleep(0.025)
        log_file.write(cmd)
        log_file.write('\n\n')  # Move to the next line in the log file
        print()  # Move to the next line in the console

    stop_background_music()
