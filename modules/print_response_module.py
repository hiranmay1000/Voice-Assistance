from utils.utils import get_log_file_path
from settings.config import assistanceName
from time import sleep

def print_response(cmd):
    log_file_path = get_log_file_path()

    with open(log_file_path, 'a') as log_file:
        log_file.write(f'{assistanceName}: ')
        for word in cmd:
            print(''.join(char for char in word), end='', flush=True)
            log_file.write(''.join(char for char in word))
            sleep(0.025)
        log_file.write('\n')  # Move to the next line in the log file
        print()  # Move to the next line in the console

print_response(["Hello", "world!"])