import requests
from utils.common import *

def createServers(token, count, name):
    set_console_title("Crypto Tools V1 | Made by ೩ Eh3an_KenZo ᶜʳʸᵖᵗᵒ | Create Servers")
    headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
    for i in range(int(count)):
        print(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}{str(i+1)}{Fore.WHITE}] Created Server")
        json = { 'name': name }
        requests.post('https://discord.com/api/v6/guilds', headers=headers, json=json)
    time.sleep(2)