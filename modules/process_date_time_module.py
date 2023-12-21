from datetime import datetime as dt
from modules.print_response_module import print_response
from modules.speech_module import talk

def process_time():
    formatted_time = dt.now().strftime("%I:%M %p")
    print_response(formatted_time)
    talk(formatted_time)

def process_date():
    formatted_date = dt.now().strftime("%d %B %Y")
    print_response(formatted_date)
    talk( "Its" + formatted_date)