from colorama import Fore

# Simple color mapper for making output less bland

def color(text, color):
    color_map = {
        'black': Fore.BLACK + text + Fore.RESET,
        'blue': Fore.BLUE + text + Fore.RESET,
        'cyan': Fore.CYAN + text + Fore.RESET,
        'green': Fore.GREEN + text + Fore.RESET,
        'magenta': Fore.MAGENTA + text + Fore.RESET,
        'red': Fore.RED + text + Fore.RESET,
        'white': Fore.WHITE + text + Fore.RESET,
        'yellow': Fore.YELLOW + text + Fore.RESET,
        'light_black': Fore.LIGHTBLACK_EX + text + Fore.RESET,
        'light_blue': Fore.LIGHTBLUE_EX + text + Fore.RESET,
        'light_cyan': Fore.LIGHTCYAN_EX + text + Fore.RESET,
        'light_green': Fore.LIGHTGREEN_EX + text + Fore.RESET,
        'light_magenta': Fore.LIGHTMAGENTA_EX + text + Fore.RESET,
        'light_red': Fore.LIGHTRED_EX + text + Fore.RESET,
        'light_white': Fore.LIGHTWHITE_EX + text + Fore.RESET,
        'light_yellow': Fore.LIGHTYELLOW_EX + text + Fore.RESET,
    }

    return color_map[color]