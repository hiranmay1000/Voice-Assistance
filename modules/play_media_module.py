import pywhatkit
from modules.speech_module import talk
from modules.print_response_module import print_response


def play_music(song):
    words_to_remove = ["can", "play", "you"]
    
    for word in words_to_remove:
        song = song.replace(word, "")

    song = song.replace("play", "")
    pywhatkit.playonyt(song)
    talk("Playing" + song + "on youtube")
    mess = 'Playing' + song
    print_response( mess)