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

pathdog = os.path.dirname(os.path.abspath(__file__))

# 使用 os.path.join 构建路径
pathopen = os.path.join(pathdog, '')

text = """

 $$$$$$\  $$\       $$\   $$\                                $$$$$$\    $$\     $$\                         $$\       
$$  __$$\ $$ |      \__|  $$ |                              $$  __$$\   $$ |    $$ |                        $$ |      
$$ /  \__|$$$$$$$\  $$\ $$$$$$\    $$$$$$\   $$$$$$\        $$ /  $$ |$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$$\ $$ |  $$\ 
\$$$$$$\  $$  __$$\ $$ |\_$$  _|  $$  __$$\ $$  __$$\       $$$$$$$$ |\_$$  _|\_$$  _|   \____$$\ $$  _____|$$ | $$  |
 \____$$\ $$ |  $$ |$$ |  $$ |    $$$$$$$$ |$$ |  \__|      $$  __$$ |  $$ |    $$ |     $$$$$$$ |$$ /      $$$$$$  / 
$$\   $$ |$$ |  $$ |$$ |  $$ |$$\ $$   ____|$$ |            $$ |  $$ |  $$ |$$\ $$ |$$\ $$  __$$ |$$ |      $$  _$$<  
\$$$$$$  |$$ |  $$ |$$ |  \$$$$  |\$$$$$$$\ $$ |            $$ |  $$ |  \$$$$  |\$$$$  |\$$$$$$$ |\$$$$$$$\ $$ | \$$\ 
 \______/ \__|  \__|\__|   \____/  \_______|\__|            \__|  \__|   \____/  \____/  \_______| \_______|\__|  \__| """                                                                                                                                                                                                                                                                                                                                                                                                
shitermaininput = """
┌──(shiter@main)-[~]
└─$"""
showtext1 = """
    •cmd           use cmd here
    •xss           XSS attack tool
    •sql           find sql bug
    •sqlmap        sqlmap tool
    •ddos          some ddos tools
    •attack flood  python flood Dos
    •exit

    input the number of tool you want to use
"""
showtext2 = """
"""
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
    tools_folder = "tools"
    target_path = os.path.join(pathdog, tools_folder)

    print(f"[yellow]{text}[/yellow]")
    print(showtext1)
    while True:
        user_input = input(shitermaininput)
        if not user_input:
            continue
        if user_input.lower() == 'exit':
            break
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'ddos':
            run_python_script(pathopen + "Tools\\ddos_Open.py")
        elif user_input.lower() == 'sql':
            run_python_script(pathopen + "\\Tools\\sql.py")
        elif user_input.lower() == 'attack flood':
            run_python_script(pathopen + "\\Tools\\psyflood.py")
        elif user_input.lower() == 'shiter attack':
            print(f'[white]{shiter}[/white]')
            time.sleep(1)
            print(f'[white]{middle}[/white]')
        elif user_input.lower() == 'xss':
            run_python_script(pathopen + "\\Tools\\xss.py")
        elif user_input.lower() == 'sqlmap':
            run_python_script(pathopen + "\\Tools\\sqlmap open.py")
        elif user_input.lower() == 'sniff':
            run_python_script(pathopen + "\\Tools\\Shiter_Snifer.py")
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

