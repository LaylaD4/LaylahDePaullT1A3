# This allows for coloured text output in the terminal.
import colorama
from colorama import Fore, Back, Style
colorama.init()


def go_back_to_main_menu():
    """Function to return to main menu without circular import error occurring."""
    from main import main_menu
    main_menu()


def ask_return_main_menu():
    """Function to allow user to decide when to return to the main menu."""
    selected = False
    while selected == False:
        selection = input(f"\n{Fore.MAGENTA}To Return to the Main Menu simply press: Enter/Return.\n")
        if selection == "":
            selected = True
            go_back_to_main_menu()