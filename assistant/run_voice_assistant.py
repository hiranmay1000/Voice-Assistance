from assistant.process_commands import process_commands
from modules.speech_module import talk
from assistant.take_cmd import take_cmd
from settings.config import is_wake_up

talk("Hello sir")

def run_voice_assistant():
    while True:
        print("\n\n\nWhile loop------------")
        command = take_cmd(5)  # Adjust the sleep timeout as needed

        if any(keyword in command for keyword in ['shut down yourself', 'shutdown yourself', 'shut yourself', 'power off yourself', 'turn off yourself']):
            talk("Shutting down")
            print("Processing request...\nShutting down...")
            break
        elif is_wake_up:
            process_commands(command)