import os
import subprocess
from rich import print
from rich.console import Console

# 设置颜色
console = Console()

logo = """

██████╗ ██████╗  ██████╗ ███████╗    ██████╗ ██╗██████╗ ██████╗ ███████╗██████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ██╔══██╗██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║  ██║██║  ██║██║   ██║███████╗    ██████╔╝██║██████╔╝██████╔╝█████╗  ██████╔╝
██║  ██║██║  ██║██║   ██║╚════██║    ██╔══██╗██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
██████╔╝██████╔╝╚██████╔╝███████║    ██║  ██║██║██║     ██║     ███████╗██║  ██║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝

                                                              ©EngineRipper
                                                              reference by Hammer

 DDos Ripper

        It is the end user's responsibility to obey all applicable laws.
        It is just like a server testing script and Your ip is visible. Please, make sure you are anonymous!

        Usage : -s 192.168.1.1 -p 443 -t 153 
        -h : -help
        -s : -server ip
        -p : -port default 80
        -q : -quiet

        -t : -turbo default 135 or 443
"""

# 使用颜色设置


print(logo)

while True:
    shitermaininput = """
┌──(shiter@main)-[DDOS Ripper]
└─$ """

    # 用户输入的参数
    user_input = input(shitermaininput)

    # 注意反斜杠的转义或使用原始字符串
    pathdog = os.path.dirname(os.path.abspath(__file__))

# 使用 os.path.join 构建路径
    # 使用 os.path.join 构建路径
    directory_path = os.path.join(pathdog, 'DDoS-Ripper-main')


    def run_sqlmap(user_input):
        try:
            # 切换到指定目录
            os.chdir(directory_path)

            command = f"python DRipper.py {user_input}"

            # 在命令行中运行命令
            subprocess.run(command, shell=True)

        except Exception as e:
            console.print(f"发生错误：{e}", style="bold red")

    # 运行程序，并将用户输入作为参数传递
    run_sqlmap(user_input)

    # 添加退出循环的条件，例如用户输入 "exit"
    if user_input.lower() == "exit":
        break
