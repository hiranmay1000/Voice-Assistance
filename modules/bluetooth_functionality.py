import subprocess
import os
from modules.speech_module import talk
from modules.print_response_module import print_response

def turn_on_bluetooth():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Specify the path to your Bash script
    bluetooth_on_script = os.path.join(script_dir, "../scripts/bluetooth_on.sh") # rfkill unblock bluetooth

    try:
        # Run the Bash script using subprocess
        print(bluetooth_on_script)
        subprocess.run(["bash", bluetooth_on_script], check=True)
        talk("Bluetooth turned on successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error turning on Bluetooth due to: {e}")

def turn_off_bluetooth():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Specify the path to your Bash script
    bluetooth_off_script = os.path.join(script_dir, "../scripts/bluetooth_off.sh") # rfkill block bluetooth

    try:
        # Run the Bash script using subprocess
        print(bluetooth_off_script)
        subprocess.run(["bash", bluetooth_off_script], check=True)
        talk("Bluetooth turned off successfully.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error turning off Bluetooth due to: {e}")

