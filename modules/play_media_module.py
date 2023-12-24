import pywhatkit
from modules.speech_module import talk
from modules.print_response_module import print_response


def play_music(song):
    if 'spotify' in song:
        talk("Sorry I don't support that, I can play on youtube instead, here you go")

    words_to_remove = ["can", "you", "play", "on", "youtube", "spotify"]
    
    for word in words_to_remove:
        song = song.replace(word, "")

    pywhatkit.playonyt(song)
    talk("Playing " + song + " on youtube")
