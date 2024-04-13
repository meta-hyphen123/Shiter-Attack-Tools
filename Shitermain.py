import os
import subprocess
import re
import urllib.parse
import time
import socket


red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
violate = "\033[1;37m"
nc = "\033[00m"



pathdog = os.path.dirname(os.path.abspath(__file__))
pathopen = os.path.join(pathdog, '')


def logo_print(total):
    print(f'''\007
{yellow}
 ____  _     _ _                 _   _   _             _    
/ ___|| |__ (_) |_ ___ _ __     / \ | |_| |_ __ _  ___| | __
\___ \| '_ \| | __/ _ \ '__|   / _ \| __| __/ _` |/ __| |/ /
 ___) | | | | | ||  __/ |     / ___ \ |_| || (_| | (__|   < 
|____/|_| |_|_|\__\___|_|    /_/   \_\__|\__\__,_|\___|_|\_\ {purple}v2.1
{cyan} =============================================
{yellow}|          Install Best Hacking Tool          |
{cyan} ============================================={nc}



{yellow}  [ 1 ] {green}XSS attack tool{yellow} [ {purple}{total} tools{yellow} ]
{yellow}  [ 2 ] {green}SQL .
{yellow}  [ 3 ] {green}sqlmap.
{yellow}  [ 4 ] {green}ddos
{yellow}  [ 5 ] {green}attack flood
{yellow}  [ 6 ] {green}web2attack
{yellow}  [ 7 ] {green}sniff
{yellow}  [ 8 ] {green}nmap
{yellow}  [ x ] {green}exit''')


shitermaininput = """
┌──(shiter@main)-[~]
└─$"""


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
    total_tools = 8  # 工具总数
    logo_print(total_tools)

    while True:
        user_input = input(shitermaininput)

        if not user_input:
            continue
        if user_input.lower() == 'x':
            break

        elif user_input.lower() == '4':
            run_python_script(pathopen + "Tools\\ddos_Open.py")
        elif user_input.lower() == '8':
            run_python_script(pathopen + "Tools\\nmap_scan.py")

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
            xss_folder_path = os.path.join(pathdog, "Tools\\web2attack-master")
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
