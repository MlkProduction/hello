from colorama import Fore, init


def say_hello():
    init(autoreset=True)
    print(Fore.RED + "Hello, world!")
