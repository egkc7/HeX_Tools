import time
import requests
from utils.common import *

def get_all_friends(token):
    set_console_title("Crypto Tools V1 | Made by ೩ Eh3an_KenZo ᶜʳʸᵖᵗᵒ | Get Friends")
    headers = {"authorization": token, "user-agent": "bruh6/9"}
    r = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    )
    print("\n")
    for friend in r.json():
        print(f"{Fore.WHITE}[ {Fore.LIGHTCYAN_EX}C {Fore.WHITE}] {friend['user']['username']}#{friend['user']['discriminator']}")
    time.sleep(2)
    print("\n")
    input("Press any key to continue...")