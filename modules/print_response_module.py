from settings.config import assistanceName
from time import sleep

def print_response(cmd):
    print(assistanceName + ':', end = ' ')
    for word in cmd:
        print(''.join(char for char in word), end='', flush=True)
        sleep(0.025)
