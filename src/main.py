'''This python library allows for a list function output for the user to use arrow keys to move up & down menu items.'''
import inquirer

'''Import file for function: create_employee to run.'''
from create_employee import create_employee

'''Import file for function: list_all_employees to run'''
from list_all_employees import list_all_employees

'''Import file for function: create_employee to run.'''
from edit_employee import edit_employee

'''Import file for function: list_all_employees to run'''
from delete_employee import delete_employee

'''Import file for function: list_one_employee to run.'''
from list_one_employee import list_one_employee

'''Import file for function: data_statistics_search to run'''
from data_statistics_search import data_statistics_search

'''Import file for function: print_employee_list to run'''
from print_employee_list import print_employee_list

'''Centres output in terminal'''
from print_centre import print_centre

print("\n")
print_centre("Welcome to the 'Initech 'Employee Application Database.")

def main_menu():
    print("\n")
    print_centre("MAIN MENU") 
    print("\n")
    
    questions = [
    inquirer.List(
        "Menu Options",
        message="Please select from the following options using the arrow keys, and press enter.",
        choices=["Display all Employees", "List an Employee", "Create an Employee", "Edit an existing Employee", "Delete an existing Employee", "Employee Data Statistics", "Print Employee List to File", "Exit Database"],)]
    answers = inquirer.prompt(questions)
    
    if answers["Menu Options"] == "Display all Employees":
        list_all_employees()
    if answers["Menu Options"] == "List an Employee":
        list_one_employee()
    if answers["Menu Options"] == "Create an Employee":
        create_employee() 
    if answers["Menu Options"] == "Edit an existing Employee":
        edit_employee()
    if answers["Menu Options"] == "Delete an existing Employee":
        delete_employee()
    if answers["Menu Options"] == "Employee Data Statistics":
        data_statistics_search()
    if answers["Menu Options"] == "Print Employee List to File":
        print_employee_list()
    if answers["Menu Options"] == "Exit Database":  
        exit()    
    else:
        main_menu()


main_menu()        