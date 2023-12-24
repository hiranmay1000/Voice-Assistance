from modules.assistant_owner_info_module import process_name_req
from modules.assistant_owner_info_module import get_boss_info
from modules.process_date_time_module import process_time
from modules.process_date_time_module import process_date
from modules.bluetooth_functionality import turn_off_bluetooth
from modules.bluetooth_functionality import turn_on_bluetooth
from modules.process_jokes_module import process_joke
from modules.dictionary_module import process_dictionary
from modules.play_media_module import play_music
from modules.wikipedia_module import search_wiki
from modules.speech_module import talk
from settings.config import assistanceName


def process_commands(cmd):

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
    elif any(keyword in cmd for keyword in ['what is the meaning', 'meaning of', 'do you know the meaning', 'meaning', 'means']):
        process_dictionary(cmd)
    elif any(keyword in cmd for keyword in ['who', 'what is', 'you know', 'called']):
        search_wiki(cmd)
    elif any(keyword in cmd for keyword in ['turn off bluetooth', 'bluetooth off', 'bluetooth turn off']):
        turn_off_bluetooth()
    elif any(keyword in cmd for keyword in ['turn on bluetooth', 'bluetooth on', 'bluetooth turn on']):
        turn_on_bluetooth()
    elif cmd != "":
        talk("Sorry I don't have that information as of now")