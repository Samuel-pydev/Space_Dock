import subprocess
import psutil
import json
import os

def manage_space(space_name):
    # 1. Load the configuratio"C:\Users\Samuel\Documents\spaces"n
    config_path = f"spaces\{space_name}.json"
    if not os.path.exists(config_path):
        print(f"Error: {space_name} space not found!")
        return

    with open(config_path, 'r') as config_file:
        config = json.load(config_file)

    # 2. Cleanup: Close "Distracting" apps defined in the config
    print(f"--- Switching to {space_name} ---")
    for process in psutil.process_iter(['name']):
        if process.info['name'] in config.get('close_apps', []):
            print(f"Closing {process.info['name']}...")
            process.terminate()

    # 3. Setup: Launch "Required" apps
    for app in config.get('launch_apps', []):
        print(f"Launching {app}...")
        subprocess.Popen(app, shell=True)

# Example usage
if __name__ == "__main__":
    # You'll call this from your UI later
    manage_space("code")