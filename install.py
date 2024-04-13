import os
import subprocess
import time

# 定义土黄色 ANSI 转义码
TAN_YELLOW = "\033[38;2;255;253;85m"
# 定义黄色 ANSI 转义码
YELLOW = "\033[93m"

# 定义变量 hellooo 并赋值为 "hello"
hellooo = "         install best hacking tool"

# 打印 hellooo 的值，加入土黄色装饰
logo = """
 ____  _     _ _                 _   _   _             _    
/ ___|| |__ (_) |_ ___ _ __     / \ | |_| |_ __ _  ___| | __
\___ \| '_ \| | __/ _ \ '__|   / _ \| __| __/ _` |/ __| |/ /
 ___) | | | | | ||  __/ |     / ___ \ |_| || (_| | (__|   < 
|____/|_| |_|_|\__\___|_|    /_/   \_\__|\__\__,_|\___|_|\_\\

"""
ask = """
  [ + ] Use It At Your Own Risk.
  [ + ] No Warranty.
  [ + ] Use it legal purpose only.
  [ + ] We are not responsible for your actions.
  [ + ] Do not do things that are forbidden.
  
 If you are installing these modules,
 that means you are agree with all terms.
"""
print(TAN_YELLOW + logo + "\033[0m ")
print("""============================================================""")
print(TAN_YELLOW + hellooo + "\033[0m ")
print("""============================================================""")
print(ask)
print("""------------------------------------------------------------""")
print("""============================================================""")

user_input = input (YELLOW + "Do you want to install Shiter modules [Y/n]>" + "\033[0m ")

def run_installation():
    finish = ""
    cmdinstall = """
    pip install tqdm
    pip install rich
    pip install scapy
    pip install requests
    """
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

if user_input.lower() == 'y':
    run_installation()
else:
    exit()