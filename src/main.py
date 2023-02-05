'''This python library allows for a list function output for the user to use arrow keys to move up & down menu items.'''
import inquirer

'''Import file for function: create_employee to run.'''
from create_employee import create_employee

print("\n")
print("Welcome to the 'Initech 'Employee Application Database.")

def main_menu():
    print("\n")
    print("MAIN MENU") 
    print("\n")
    
    questions = [
    inquirer.List(
        "Menu Options",
        message="Please select from the following options using the arrow keys, and press enter.",
        choices=["Display all Employees", "List an Employee", "Create an Employee", "Edit an existing Employee", "Delete an existing Employee", "Employee Data Statistics", "Print Employee List to File", "Exit Database"],)]
    answers = inquirer.prompt(questions)
    
    if answers["Menu Options"] == "Display all Employees":
        pass
    if answers["Menu Options"] == "List an Employee":
        pass
    if answers["Menu Options"] == "Create an Employee":
        create_employee() 
    if answers["Menu Options"] == "Edit an existing Employee":
        pass
    if answers["Menu Options"] == "Delete an existing Employee":
        pass
    if answers["Menu Options"] == "Employee Data Statistics":
        pass 
    if answers["Menu Options"] == "Print Employee List to File":
        pass
    if answers["Menu Options"] == "Exit Database":  
        exit()    
    else:
        main_menu()


main_menu()        