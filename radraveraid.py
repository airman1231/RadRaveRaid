def Clear():
    try:
        os.system('cls')  # For Windows
    except:
        os.system('clear')  # For Unix-based systems

def Setup():
    try:
        ctypes.windll.kernel32.SetConsoleTitleW(f'[RadRaveRaid v{INIT.__version__}] | By Fawful')
    except AttributeError:
        # ctypes.windll is not available on non-Windows systems
        pass
    
    counttokens = len(open('tokens.txt').readlines())
    countproxies = len(open('proxies.txt').readlines())

    print(f'''{Fore.RESET}                {Fore.MAGENTA}    ____            __{Fore.RESET}{Fore.CYAN}   ____                 {Fore.RESET}{Fore.RED}     ____        _     __{Fore.RESET}
                {Fore.MAGENTA}   / __ \____ _____/ /{Fore.RESET}{Fore.CYAN}  / __ \____ __   _____ {Fore.RESET}{Fore.RED}    / __ \____ _(_)___/ /{Fore.RESET}
                {Fore.MAGENTA}  / /_/ / __ `/ __  / {Fore.RESET}{Fore.CYAN} / /_/ / __ `/ | / / _ \{Fore.RESET}{Fore.RED}   / /_/ / __ `/ / __  / {Fore.RESET}
                {Fore.MAGENTA} / _, _/ /_/ / /_/ /  {Fore.RESET}{Fore.CYAN}/ _, _/ /_/ /| |/ /  __/{Fore.RESET}{Fore.RED}  / _, _/ /_/ / / /_/ /  {Fore.RESET}
                {Fore.MAGENTA}/_/ |_|\__,_/\__,_/  {Fore.RESET}{Fore.CYAN}/_/ |_|\__,_/ |___/\___/ {Fore.RESET}{Fore.RED} /_/ |_|\__,_/_/\__,_/   {Fore.RESET}


                       {Fore.CYAN}RadRaveRaid {INIT.__version__} {Fore.RESET}| Because fuck you
                       {Fore.CYAN}Type {Fore.RESET}"help"{Fore.CYAN} for a list of commands
                       {Fore.GREEN}{counttokens}{Fore.RESET}{Fore.CYAN} tokens loaded!
                       {Fore.GREEN}{countproxies}{Fore.RESET}{Fore.CYAN} proxies loaded!
                       {Fore.MAGENTA}Created by {Fore.RESET}Fawful | {Fore.CYAN}Special thx to {Fore.RESET}Humble#8292{Fore.CYAN}, {Fore.RED}RaidToolBox{Fore.CYAN}, and {Fore.YELLOW}h0nda
                       {Fore.MAGENTA}https://github.com/{Fore.RESET}riaaaaaaaa
''' + Fore.RESET)
