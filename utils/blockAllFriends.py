import requests
from utils.common import *

def blockAllFriends(token):
    set_console_title("Crypto Tools V1 | Made by ೩ Eh3an_KenZo ᶜʳʸᵖᵗᵒ | Block All Friends")
    headers = {"authorization": token, "user-agent": "bruh6/9"}
    json = {"type": 2}
    block_friends_request = requests.get("https://canary.discord.com/api/v8/users/@me/relationships", headers=headers).json()
    for i in block_friends_request:
        requests.put(
            f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
            headers=headers,
            json=json,
        )
        print(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}C{Fore.WHITE}] Blocked Friend | {i['id']}")