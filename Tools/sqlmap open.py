import os
import subprocess
from rich import print
from rich.console import Console

# 设置颜色
console = Console()

logo = """
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.7.11.3#dev}
|_ -| . [.]     | .'| . |
|___|_  [.]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org
"""

# 使用颜色设置
colored_logo = f"[bold #CF6417]{logo}[/bold #CF6417]"

print(colored_logo)

while True:
    shitermaininput = """
┌──(shiter@main)-[sqlmap]
└─$ """

    # 用户输入的参数
    user_input = input(shitermaininput)

    # 注意反斜杠的转义或使用原始字符串
    pathdog = os.path.dirname(os.path.abspath(__file__))

# 使用 os.path.join 构建路径
    directory_path = os.path.join(pathdog, '')

    def run_sqlmap(user_input):
        try:
            # 切换到指定目录
            os.chdir(directory_path)

            # 构建命令，将用户输入作为参数传递给 sqlmap.py
            command = f"python sqlmap.py {user_input}"

            # 在命令行中运行命令
            subprocess.run(command, shell=True)

        except Exception as e:
            console.print(f"发生错误：{e}", style="bold red")

    # 运行程序，并将用户输入作为参数传递
    run_sqlmap(user_input)

    # 添加退出循环的条件，例如用户输入 "exit"
    if user_input.lower() == "exit":
        break
