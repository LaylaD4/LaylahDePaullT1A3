'''This allows for coloured text output in the terminal.'''
import colorama
from colorama import Fore, Back, Style
colorama.init()

'''To return to main menu need to import that without circular import error.'''
def go_back_to_main_menu():
    from main import main_menu
    main_menu()


'''Allows the user to decide when to return to the main menu.'''
def ask_return_main_menu():
    selected = False
    while selected == False:
        selection = input(f"\n{Fore.MAGENTA}To Return to the Main Menu simply press:\n")
        if selection == "":
            selected = True
            go_back_to_main_menu()