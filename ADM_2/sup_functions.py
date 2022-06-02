from colorama import init, Fore

def fact_(a):
    result = 1
    for i in range(1, a+1):
        result*= i
    return result
 
def print_green_text(text):
     print(Fore.GREEN + text)
     print(Fore.WHITE)

def print_yellow_text(text):
     print(Fore.YELLOW + text)
     print(Fore.WHITE)

def print_red_text(text):
    print(Fore.RED + text)
    print(Fore.WHITE)

def print_blue_text(text):
    print(Fore.LIGHTCYAN_EX + text)
    print(Fore.WHITE)

def print_im_text(text):
    print(Fore.LIGHTMAGENTA_EX + text)
    print(Fore.WHITE)
