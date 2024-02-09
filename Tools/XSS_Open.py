import os
import subprocess
import re
import tkinter as tk
from tkinter import filedialog
from rich import print
import urllib
from urllib.parse import urlparse
import time
import socket
import sys
import os
import time
from tqdm import tqdm
import random
from rich import print
from colorama import Fore, Style  
from rich.console import Console
import urllib.parse

console = Console()

pathdog = os.path.dirname(os.path.abspath(__file__))
pathopen = os.path.join(pathdog, '')

text = r'''
 __  __             _   _   _             _    
 \ \/ /___ ___     / \ | |_| |_ __ _  ___| | __
  \  // __/ __|   / _ \| __| __/ _` |/ __| |/ /
  /  \\__ \__ \  / ___ \ |_| || (_| | (__|   < 
 /_/\_\___/___/ /_/   \_\__|\__\__,_|\___|_|\_\
                                               '''
yellow_text = f"[#FFFD55]{text}[/]"
shitermaininput = """
┌──(shiter@XSS)-[~\Tools\XSS]
└─$"""

showtext1 = """
     [1] XSS-LOADER TOOLS  xss payload generator
     [2] XSSCon
     [3] XSStrike
     [4] XanXss
     [5] exit
==========================================================="""

dooo = """    input the number of tool you want to use"""
yellow_do = f"[#FFFD55]{dooo}[/]"

dogg = """==========================================================="""
showtext2 = """ """
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

def main():
    tools_folder = "tools"
    target_path = os.path.join(pathdog, tools_folder)

    console.print(yellow_text)
    print(f"[red]{showtext2}[/red]")
    console.print(showtext1)
    console.print(yellow_do)
    console.print(dogg)
    while True:
        user_input = input(shitermaininput)
        if not user_input:
            continue
        if user_input.lower() == '5':
            break
        elif user_input.lower() == '3':
            xss_folder_path = os.path.join(pathdog,"XSStrike-master")
            os.chdir(xss_folder_path)
            run_python_script("xsstrike.py")
        elif user_input.lower() == '4':
            xss_folder_path = os.path.join(pathdog,"XanXSS-master")
            os.chdir(xss_folder_path)
            run_python_script("xan.py")
        elif user_input.lower() == '2':
            xss_folder_path = os.path.join(pathdog,"XSSCon-master")
            os.chdir(xss_folder_path)
            run_python_script("xsscon.py")
        elif user_input.lower() == '1':
            xss_folder_path = os.path.join(pathdog,"xss")
            os.chdir(xss_folder_path)
            run_python_script("payloader.py")
        else:
            result = run_command(user_input)
            print(result)

if __name__ == "__main__":
    main()
