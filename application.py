import os
from settings.config import username
from assistant.run_voice_assistant import run_voice_assistant


try:
    # When checking for the operating system type in Python, os.name can have different values depending on the underlying operating system.
    # On POSIX-compatible systems (like Linux or macOS), os.name is set to 'posix'. On Windows, it is set to 'nt'

    if os.name == 'posix':
        os.environ['DISPLAY'] = ':0'
        os.system(f'xhost +SI:localuser:{username}')

    run_voice_assistant()

    print("\nProgram execution complete.")

except Exception as e:
    print(f"An error occurred: {e}")


print("\nProgram execution complete.")