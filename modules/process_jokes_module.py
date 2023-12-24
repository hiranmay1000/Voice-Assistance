import pyjokes as jokes
from modules.print_response_module import print_response
from modules.speech_module import talk


def process_joke():
    joke = jokes.get_joke()
    talk(joke)
