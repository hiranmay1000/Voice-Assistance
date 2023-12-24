from datetime import datetime as dt
from modules.print_response_module import print_response
from modules.speech_module import talk

def process_time():
    formatted_time = dt.now().strftime("%I:%M %p")
    talk(formatted_time)

def process_date():
    formatted_date = dt.now().strftime("%d %B %Y")
    talk( "It's " + formatted_date)