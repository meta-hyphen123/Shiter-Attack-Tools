import os
import subprocess

logo = """
  ____       _                       _     _ _            
 / ___|  ___| |_   _   _ _ __    ___| |__ (_) |_ ___ _ __ 
 \___ \ / _ \ __| | | | | '_ \  / __| '_ \| | __/ _ \ '__|
  ___) |  __/ |_  | |_| | |_) | \__ \ | | | | ||  __/ |   
 |____/ \___|\__|  \__,_| .__/  |___/_| |_|_|\__\___|_|   
                        |_|                               """

print(logo)

finish = """
  ____       _                                                  __       _ _          __ _       _     _              _ 
 / ___|  ___| |_ _   _ _ __    ___ _   _  ___ ___ ___  ___ ___ / _|_   _| | |_   _   / _(_)_ __ (_)___| |__   ___  __| |
 \___ \ / _ \ __| | | | '_ \  / __| | | |/ __/ __/ _ \/ __/ __| |_| | | | | | | | | |_| | '_ \| / __| '_ \ / _ \/ _` |
  ___) |  __/ |_| |_| | |_) | \__ \ |_| | (_| (_|  __/\__ \__ \  _| |_| | | | |_| | |  _| | | | | \__ \ | | |  __/ (_| |
 |____/ \___|\__|\__,_| .__/  |___/\__,_|\___\___\___||___/___/_|  \__,_|_|_|\__, | |_| |_|_| |_|_|___/_| |_|\___|\__,_|
                      |_|                                                    |___/                                      """

cmdinstall = """
pip install tqdm
pip install rich
pip install socket
pip install colorama
pip install urllib
pip install colorama
pip install threading
pip install scapy
pip install requests
pip install random
"""

def run_installation():
    try:
        # Save installation commands to a temporary batch file
        with open("install_commands.bat", "w") as batch_file:
            batch_file.write(cmdinstall)

        # Open a separate CMD window and run the batch file
        subprocess.run(["start", "cmd", "/c", "install_commands.bat"], shell=True)

        # Wait for the CMD window to complete
        subprocess.run(["timeout", "/nobreak", "/t", "10"], shell=True)  # Adjust the timeout as needed

        print(finish)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_installation()
