import pywhatkit

def play_music(song):
    words_to_remove = ["can", "play", "you"]
    
    for word in words_to_remove:
        song = song.replace(word, "")

    song = song.replace("play", "")
    pywhatkit.playonyt(song)
    talk("Playing" + song + "on youtube")
    mess = 'Playing' + song
    print_response(mess)