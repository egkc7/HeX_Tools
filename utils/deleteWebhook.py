import requests
from utils.common import *

def deleteWebhook(url):
    set_console_title("Crypto Tools V1 | Made by ೩ Eh3an_KenZo ᶜʳʸᵖᵗᵒ | Delete Webhook")
    requests.delete(url)
    print(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}C{Fore.WHITE}] Deleted Webhook")
    sleep(1)