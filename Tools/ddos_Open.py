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

console = Console()

# 获取当前脚本所在文件夹的路径
pathdog = os.path.dirname(os.path.abspath(__file__))

# 使用 os.path.join 构建路径
pathopen = os.path.join(pathdog, '')

text =r'''
  ____  ____              _____           _     
 |  _ \|  _ \  ___  ___  |_   _|__   ___ | |___ 
 | | | | | | |/ _ \/ __|   | |/ _ \ / _ \| / __|
 | |_| | |_| | (_) \__ \   | | (_) | (_) | \__ \
 |____/|____/ \___/|___/   |_|\___/ \___/|_|___/
                                                '''
yellow_text = f"[#FFFD55]{text}[/]"
shitermaininput = """
┌──(shiter@main)-[ddos~contrl]
└─$"""
showtext1 = """
    [1]ddos
    [2]dos
    [3]loic
    [4]hulk
    [5]hulk-gui
    [6]WTF DDos
    [7]ddos-ripper
    [8]slowloris
    [9]exit

==========================================================="""

dooo = """    input the number of tool you want to use"""
yellow_do = f"[#FFFD55]{dooo}[/]"

dogg = """==========================================================="""
showtext2 = """ """
def about_url(url):
    try:
        parsed_url = urllib.parse.urlparse(url)
        host = parsed_url.hostname

        # Fetch IP address
        ip = socket.gethostbyname(host)

        # Determine the port based on the URL scheme
        if parsed_url.scheme == 'http':
            port = 80
        elif parsed_url.scheme == 'https':
            port = 443
        else:
            print("Unsupported URL scheme.")
            return

        # Print information to the console
        print(f"URL: {url}\nIP Address: {ip}\nPort: {port}")

    except Exception as e:
        # Handle any errors that may occur
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

def run_python_script11(script_path):
    try:
        subprocess.run(["python", script_path], check=True)
    except FileNotFoundError:
        print(f"Python interpreter not found. Make sure Python is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Python script: {e}")


def main():
    # 切换到指定目录
    os.chdir(r"C:\Users\Joe Lu\Desktop\Shiter\Tools")

    console.print(yellow_text)
    print(f"[red]{showtext2}[/red]")
    console.print(showtext1)
    console.print(yellow_do)
    console.print(dogg)
    while True:
        user_input = input(shitermaininput)
        if not user_input:
            continue
        if user_input.lower() == '9':
            break
        elif user_input.lower() == '1':
            run_python_script(pathopen + "\\ddos-attack.py")
        elif user_input.lower() == '8':
            run_python_script(pathopen + "\\slowloris.py")
        elif user_input.lower() == '2':
            run_python_script(pathopen + "\\start.py")
        elif user_input.lower() == '5':
            run_python_script(pathopen + "\\hulk-gui.py")
        elif user_input.lower() == '4':
            run_python_script(pathopen + "\\hulk.py")
        elif user_input.lower() == '6':
            run_python_script(pathopen + "\\WTF.py")
        elif user_input.lower() == '7':
            run_python_script(pathopen + "\\DRipper.py")
        elif user_input.lower() == '3':
            print("try input “LOIC”")
        elif user_input.lower().startswith('about '):
            # 提取用户输入中的URL
            url_input = user_input[6:]
            about_url(url_input)
        elif user_input.lower().startswith('dos '):
            # 使用正则表达式匹配dos命令
            dos_match = re.match(r'dos\s+(\S+)\s+-p\s+(\d+)', user_input.lower())
            if dos_match:
                ip = dos_match.group(1)
                port = dos_match.group(2)
                # 构建Dos.py命令并执行
                dos_command = f"python C:\\Users\\Joe Lu\\Desktop\\Shiter\\Dos.py -t {ip} -r 10000 -p {port}"
                result = run_command(dos_command)
                print(result)
            else:
                print("Invalid dos command format. Example: dos <IP> -p<port>")
        else:
            result = run_command(user_input)
            print(result)

if __name__ == "__main__":
    main()

