'''Checks that input from user is a number character, and handles float inputs.'''
def check_for_valid_number(message):
    number = None
    while number == None:
        try:
            number = float(input(message))
            return int(number)
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
        elif entry.isdigit():
            entry = ""
            try: 
                raise ValueError("You entered a number, please enter a name this time.")
            except ValueError as warning:
                print(f"{warning}\n")
        else:
            return entry