import random
from modules.speech_module import talk
from settings.config import assistanceName
from modules.print_response_module import print_response

def process_name_req():
    mess = ["No doubt about it", "Definately I like my name " + assistanceName, "Yes I got a very cool name", "Yes I like it", "I like my name very much"]

    selected_mess = random.choice(mess)
    print_response(selected_mess)
    talk(selected_mess)

def get_boss_info():
    mess = "My boss is Mr Hiranmay, and he assigned me this name"
    talk(mess)
    print(mess)