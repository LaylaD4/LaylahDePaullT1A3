# Use regex to check just alphabetical letter input.
import re 

# This allows for coloured text output in the terminal.
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def check_for_valid_number(message, number_type):
    """Checks that input from user is a number character, and handles float inputs.

    :param message: A message asking user for either age or salary input.
    :param number_type: age or salary.
    """
    number = None
    while number == None:
        try:
            number = float(input(message))
            number = handle_number_errors(number, number_type)
            if number == False:
                return check_for_valid_number(message, number_type)
            else:    
                return number
        except ValueError:
            print(f"\n{Fore.MAGENTA}You did not enter a valid number. Please try again.\n")


def check_for_valid_string(message): 
    """Checks that input from user is an alphabet character.

    :param message: A message asking user for either name, or role input.
    """
    entry = ""
    while entry == "":
        entry = input(message)
        if entry == "": 
            try: 
                raise ValueError("You did not make an entry, please try again.")
            except ValueError as warning:
                print(f"\n{Fore.MAGENTA}{warning}\n")     
        elif only_letters(entry) == False:
            entry = ""
            try: 
                raise ValueError("Invalid entry, please enter only letters for the name this time.")
            except ValueError as warning:
                print(f"\n{Fore.GREEN}{warning}\n")
        else:
            return entry


def only_letters(string):
    """Checks that only letters are entered using regex, and re import.
    
    :param string: user input for name, or role.
    """
    return bool(re.match("^[a-zA-Z_ ]+$", string)) 


def handle_number_errors(number, number_type):
    """Checks that age or salary entered is over 18 or 42000.

    :param number: The number input from user.
    :param number_type: age or salary.
    """
    number = int(number)
    if number >= 18 and number_type == "age":
        return number 
    elif number >= 42000 and number_type == "salary":
        return number 
    else:
        if number_type == "age":
            print(f"{Fore.GREEN}\nPlease enter an age that is: 18 or above.\n")
        else:
            print(f"{Fore.GREEN}\nPlease enter a salary that is: 42000 (minimum wage) or above.\n")
        return False               