import os
from rich import print
from scapy.all import sniff
import socket

# 获取当前系统颜色设置
previous_color = os.system("color")

# 设置终端背景颜色为白色
os.system("color 07") 

# 插入你自己的代码这里
def sniff_packets():
    # Define a callback function to process each captured packet
    def process_packet(packet):
        # Check if the packet contains network content from others
            print(f'[green]{packet.summary()}[/green]')
    
    # Start sniffing packets on the network interface
    sniff(prn=process_packet, store=False)


# Run the packet sniffer
if __name__ == "__main__":
    sniff_packets()
