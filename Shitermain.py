import os
import subprocess
import re
import tkinter as tk
from tkinter import filedialog
from rich import print
import urllib
from urllib.parse import urlparse
import time
import socket  # Add this import for the socket module
import sys
import os
import time
from tqdm import tqdm
import socket
import random
from rich import print
from colorama import Fore, Style  
from rich.console import Console
import urllib.parse  # Add this import
from colorama import Fore, Style

console = Console()

pathdog = os.path.dirname(os.path.abspath(__file__))
pathopen = os.path.join(pathdog, '')

text = r'''
 ____  _     _ _                 _   _   _             _    
/ ___|| |__ (_) |_ ___ _ __     / \ | |_| |_ __ _  ___| | __
\___ \| '_ \| | __/ _ \ '__|   / _ \| __| __/ _` |/ __| |/ /
 ___) | | | | | ||  __/ |     / ___ \ |_| || (_| | (__|   < 
|____/|_| |_|_|\__\___|_|    /_/   \_\__|\__\__,_|\___|_|\_\
'''

dog = r'''============================================================'''

eee = '''                   Best Hacking Tool'''
yellow_text = f"[#FFFD55]{text}[/]"

yellow_eee = f"[#FFFD55]{eee}[/]"


shitermaininput = """
┌──(shiter@main)-[~]
└─$"""

showtext1 = f"""
    cmd              use cmd here
    [1]xss           XSS attack tool
    [2]sql           find sql bug
    [3]sqlmap        sqlmap tool
    [4]ddos          some ddos tools
    [5]attack flood  python flood Dos
    [6]web2attck
    [7]sniffer
    [8]exit

==========================================================="""

dooo = """    input the number of tool you want to use"""
yellow_do = f"[#FFFD55]{dooo}[/]"

dogg = """==========================================================="""
showtext2 = ""
def about_url(url):
    try:
        parsed_url = urllib.parse.urlparse(url)
        host = parsed_url.hostname

        ip = socket.gethostbyname(host)

        if parsed_url.scheme == 'http':
            port = 80
        elif parsed_url.scheme == 'https':
            port = 443
        else:
            print("Unsupported URL scheme.")
            return

        print(f"URL: {url}\nIP Address: {ip}\nPort: {port}")

    except Exception as e:
        print(f"Error fetching information: {str(e)}")

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        output = result.stdout if result.stdout else result.stderr
        return output
    except Exception as e:
        return f"Error running command: {str(e)}"

def run_python_script(script_path):
    try:
        subprocess.run(["python", script_path], check=True)
    except FileNotFoundError:
        print(f"Python interpreter not found. Make sure Python is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Python script: {e}")

def run_dogshit(script_path):
    try:
        subprocess.run(["python", script_path], check=True)
    except FileNotFoundError:
        print(f"Python interpreter not found. Make sure Python is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Python script: {e}")

def run_python_script11(script_path):
    try:
        subprocess.run(["cd", script_path], check=True)
    except FileNotFoundError:
        print(f"Python interpreter not found. Make sure Python is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Python script: {e}")
def main():
    tools_folder = "tools"
    target_path = os.path.join(pathdog, tools_folder)

    console.print(yellow_text)
    console.print(dog)
    console.print(yellow_eee)
    console.print(dog)
    console.print(showtext1)
    console.print(yellow_do)
    console.print(dogg)
    
    
    while True:
        user_input = input(shitermaininput)
        
        if not user_input:
            continue
        if user_input.lower() == '8':
            break
            
            
        elif user_input.lower() == '4':
            run_python_script(pathopen + "Tools\\ddos_Open.py")
            
        elif user_input.lower() == '2':
            run_python_script(pathopen + "\\Tools\\sql.py")
            
        elif user_input.lower() == '5':
            run_python_script(pathopen + "\\Tools\\psyflood.py")
            
        elif user_input.lower() == '3':
            run_python_script(pathopen + "\\Tools\\sqlmap open.py")
            
        elif user_input.lower() == '7':
            run_python_script(pathopen + "\\Tools\\Shiter_Snifer.py")
            
        elif user_input.lower() == '1':
            run_python_script(pathopen + "\\Tools\\XSS_Open.py")
            
        elif user_input.lower() == '6':
            xss_folder_path = os.path.join(pathdog,"Tools\\web2attack-master")
            os.chdir(xss_folder_path)
            run_python_script("w2aconsole.py")
            
        elif user_input.lower().startswith('about '):
            url_input = user_input[6:]
            about_url(url_input)
            
        elif user_input.lower().startswith('dos '):
            dos_match = re.match(r'dos\s+(\S+)\s+-p\s+(\d+)', user_input.lower())
            if dos_match:
                ip = dos_match.group(1)
                port = dos_match.group(2)
                dos_command = f"python C:\\Users\\Joe Lu\\Desktop\\Shiter\\Dos.py -t {ip} -r 10000 -p {port}"
                result = run_command(dos_command)
                console.print(result)
            else:
                console.print("Invalid dos command format. Example: dos <IP> -p<port>")
                
        else:
            result = run_command(user_input)
            console.print(result)

if __name__ == "__main__":
    main()
