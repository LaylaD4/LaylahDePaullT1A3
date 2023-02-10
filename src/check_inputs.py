'''Use regex to check string input'''
import re 

'''Checks that input from user is a number character, and handles float inputs.'''
def check_for_valid_number(message, number_type):
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
            print("That is not a number. Please try again.\n")

'''Checks that input from user is an alphabet character.'''
def check_for_valid_string(message): 
    entry = ""
    while entry == "":
        entry = input(message)
        if entry == "": 
            try: 
                raise ValueError("You did not make an entry, please try again.")
            except ValueError as warning:
                print(f"{warning}\n")     
        elif only_letters(entry) == False:
            entry = ""
            try: 
                raise ValueError("You entered a number, please enter a name this time.")
            except ValueError as warning:
                print(f"{warning}\n")
        else:
            return entry

'''Checks that only letters are entered using regex, and re import'''
def only_letters(string):
    return bool(re.match("^[a-zA-Z_ ]+$", string)) 

'''Checks that any age or salary entered is over 18, and 42000 respectively'''
def handle_number_errors(number, number_type):
    number = int(number)
    if number >= 18 and number_type == "age":
        return number 
    elif number >= 42000 and number_type == "salary":
        return number 
    else:
        if number_type == "age":
            print("Please enter an age that is: 18 or above.\n")
        else:
            print("Please enter a salary that is: 42000 (minimum wage) or above.\n")
        return False               