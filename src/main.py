'''This python library allows for a list function output for the user to use arrow keys to move up & down menu items.'''
import inquirer

'''This allows for coloured text output in the terminal.'''
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

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

'''Alows for bash script input'''
from sys import argv

'''Import datetime module to get current date.'''
from datetime import date

'''Returns full name from bash script'''
def get_full_name():
    i = 1
    name = ""
    while i < len(argv):
        name = name + argv[i] + " "
        i = i + 1
    return name

# Log in details:
print(f"\n{Fore.BLACK}{Style.BRIGHT}Logged In: {Fore.BLUE}{get_full_name().title()} \n{Fore.BLACK}{Style.BRIGHT}Date: {Fore.BLUE}{date.today()}")    

print("\n")
print_centre(f"{Fore.GREEN}{Style.BRIGHT}Hello {Fore.MAGENTA}{get_full_name().title()}{Fore.GREEN}Welcome to the 'Initech' Employee Database Application.")

def main_menu():
    print("\n")
    print_centre(f"{Fore.MAGENTA}MAIN MENU") 
    print("\n")
    
    questions = [
    inquirer.List(
        "Menu Options",
        message=f"{Fore.CYAN}Please select from the following options using the arrow keys, and press enter.",
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
        print(f"\n{Fore.BLACK}{Style.BRIGHT}Logged Out: {Fore.BLUE}{get_full_name().title()} \n{Fore.BLACK}{Style.BRIGHT}Date: {Fore.BLUE}{date.today()}\n")
        exit()    
    else:
        main_menu()


main_menu()

