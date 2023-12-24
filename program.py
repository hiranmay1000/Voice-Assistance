import os
from settings.config import username

# When checking for the operating system type in Python, os.name can have different values depending on the underlying operating system. On POSIX-compatible systems (like Linux or macOS), os.name is set to 'posix'. On Windows, it is set to 'nt'

if os.name == 'posix':
    os.environ['DISPLAY'] = ':0'
    os.system(f'xhost +SI:localuser:{username}')

from assistant.run_voice_assistant import run_voice_assistant

run_voice_assistant()

print("\n\nEnd of code...")
