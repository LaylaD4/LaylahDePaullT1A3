# This allows for a list function output for the user to use arrow keys to move up & down menu.
import inquirer

# This allows for coloured text output in the terminal.
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# This allows for shell commands in the terminal.
import os

# Import file for function: create_employee to run.
from create_employee import create_employee

# Import file for function: list_all_employees to run
from list_all_employees import list_all_employees

# Import file for function: create_employee to run.
from edit_employee import edit_employee

# Import file for function: list_all_employees to run
from delete_employee import delete_employee

# Import file for function: list_one_employee to run.
from list_one_employee import list_one_employee

# Import file for function: data_statistics_search to run.
from data_statistics_search import data_statistics_search

# Import file for function: print_employee_list to run'''
from print_employee_list import print_employee_list

# Centres output in terminal
from print_centre import print_centre

# Alows for bash script argument
from sys import argv

# Import datetime module to get current date.
from datetime import date


def get_full_name():
    """Returns full name from bash script argument"""
    i = 1
    name = ""
    while i < len(argv):
        name = name + argv[i] + " "
        i = i + 1
    return name


def main_menu():
    """Function creates the MAIN MENU options together with external python library inquirer."""
    os.system('clear')
    
    print(f"\n{Fore.BLACK}{Style.BRIGHT}Logged In: {Fore.BLUE}{get_full_name().title()} \n{Fore.BLACK}{Style.BRIGHT}Date: {Fore.BLUE}{date.today()}")    

    print("\n")
    print_centre(f"{Fore.GREEN}{Style.BRIGHT}Hello {Fore.MAGENTA}{get_full_name().title()}{Fore.GREEN}Welcome to the 'Initech' Employee Database Application.")
    print("\n")
    
    print_centre(f"{Fore.MAGENTA}MAIN MENU") 
    print("\n")
    
    questions = [
    inquirer.List(
        "Menu Options",
        message=f"{Fore.CYAN}Please select from the following options using the arrow keys, and press enter.",
        choices=["Display all Employees", "List an Employee", "Create an Employee", "Edit an Existing Employee", "Delete an Existing Employee", "Employee Data Statistics", "Print Employee List to File", "Exit Database"],)]
    answers = inquirer.prompt(questions)
    
    if answers["Menu Options"] == "Display all Employees":
        os.system('clear')
        list_all_employees()
    if answers["Menu Options"] == "List an Employee":
        os.system('clear')
        list_one_employee()
    if answers["Menu Options"] == "Create an Employee":
        os.system('clear')
        create_employee() 
    if answers["Menu Options"] == "Edit an Existing Employee":
        os.system('clear')
        edit_employee()
    if answers["Menu Options"] == "Delete an Existing Employee":
        os.system('clear')
        delete_employee()
    if answers["Menu Options"] == "Employee Data Statistics":
        os.system('clear')
        data_statistics_search()
    if answers["Menu Options"] == "Print Employee List to File":
        os.system('clear')
        print_employee_list()
    if answers["Menu Options"] == "Exit Database":
        os.system('clear')  
        print(f"\n{Fore.BLACK}{Style.BRIGHT}Logged Out: {Fore.BLUE}{get_full_name().title()} \n{Fore.BLACK}{Style.BRIGHT}Date: {Fore.BLUE}{date.today()}\n")
        exit()    
    else:
        main_menu()

main_menu()




