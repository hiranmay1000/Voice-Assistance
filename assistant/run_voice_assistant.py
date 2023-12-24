import threading
from assistant.process_commands import process_commands
from modules.speech_module import talk
from assistant.take_cmd import take_cmd
from settings.config import is_wake_up

# Create an event to signal when the voice assistant thread should stop
stop_event = threading.Event()

talk("Hello sir")

def run_voice_assistant():
    print("\n\nCode execution start------------")
    while not stop_event.is_set():
        command = take_cmd(5)  # Adjust the sleep timeout as needed

        if any(keyword in command for keyword in ['shut down yourself', 'shutdown yourself', 'shut yourself', 'power off yourself', 'turn off yourself']):
            talk("Shutting down")
            print("Processing request...\nShutting down...")
            stop_event.set()
            break
        elif is_wake_up:
            process_commands(command)

# Create a thread for the voice assistant
assistant_thread = threading.Thread(target=run_voice_assistant)

# Start the thread
assistant_thread.start()

# Continue with the main program or any other tasks while the voice assistant thread is running

# Optionally, you can set the stop_event when you want the voice assistant thread to stop
# stop_event.set()

# Check if the thread is still alive before joining
if assistant_thread.is_alive():
    assistant_thread.join()

# Continue with the main program or any other tasks after the voice assistant thread has finished
