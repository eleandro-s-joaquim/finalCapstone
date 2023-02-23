def linha(tam=76):
    return "-" * tam

def show_red_black_2(msg_1, msg_2):
    print(f"{GREEN}{linha()}{END}")
    print(f"{BACK_RED}{msg_1.upper().center(76)}{END}")
    print(f"{BACK_RED}{msg_2.upper().center(76)}{END}")
    print(f"{GREEN}{linha()}{END}")

def show_back_green(msg):
    print(f"{GREEN}{linha()}{END}")
    print(f"{BACK_GREEN}{msg.upper().center(76)}{END}")
    print(f"{GREEN}{linha()}{END}")

def show_white(msg_1, msg_2):
    print(f"{GREEN}{linha()}{END}")
    print(f"{msg_1.upper().center(76)}")
    print(f"{msg_2.upper().center(76)}")
    print(f"{GREEN}{linha()}{END}")

def show_red_black(msg):
    print(f"{GREEN}{linha()}{END}")
    print(f"{BACK_RED}{msg.upper().center(76)}{END}")
    print(f"{GREEN}{linha()}{END}")

def show_red_txt(msg):
    print(f"{GREEN}{linha()}{END}")
    print(f"{LIGHTRED}{msg.upper().center(76)}{END}")
    print(f"{GREEN}{linha()}{END}")

def show_line_green():
    print(f"{GREEN}{linha()}{END}")

def show_txt(msg):
    print((msg.upper().center(66)))

def show_cyan(msg):
    print(f"{GREEN}{linha()}{END}")
    print(f"{CYAN}{msg.upper().center(76)}{END}")
    print(f"{GREEN}{linha()}{END}")

def show_red_2(msg_1, msg_2):
    print(f"{GREEN}{linha()}{END}")
    print(f"{LIGHTRED}{msg_1.upper().center(76)}{END}")
    print(f"{LIGHTRED}{msg_2.upper().center(76)}{END}")
    print(f"{GREEN}{linha()}{END}")

END = '\033[0;0m'
BLUE = '\033[34m'
GREEN = '\033[32m'
BOLD = "\033[;1m"
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
CYAN = "\033[1;36m"
BACK_WHITE = "\033[;7m"
WARN = '\u26A0\uFE0F'
LIGHTRED = '\033[91m'
BACK_RED = '\033[41m'
BACK_GREEN = '\033[42m'
BACKGRO = '\033[42m'+'\033[1m'+'\033[31m'






