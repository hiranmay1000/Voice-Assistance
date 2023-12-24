import wikipedia as wiki

from modules.speech_module import talk
from modules.print_response_module import print_response


def search_wiki(cmd):
    words_to_remove = ["who", "is", "the", "heck", "hell", "mr", "mrs", "ms"]
    
    for word in words_to_remove:
        cmd = cmd.replace(word, "")

    try:
        output = wiki.summary(cmd, sentences=4)
        talk("Here are some results")
        print_response(output)
    except Exception as e:
        talk("Sorry! there is no information available right now!")
