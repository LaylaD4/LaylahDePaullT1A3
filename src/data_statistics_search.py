# This allows for a list function output for the user to use arrow keys to move up & down menu.
import inquirer

# This allows for coloured text output in the terminal.
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# This allows for shell commands in the terminal.
import os

# Import file for access to employee_list.
from employee import employee_list

# Allows the user to return to the main menu.
from return_main_menu import go_back_to_main_menu

# Centres output in terminal.
from print_centre import print_centre


def data_statistics_search():
    """Function creates a menu: GENERAL EMPLOYEE DATA for user to select from using arror keys."""
    print("\n")
    print_centre(f"{Fore.MAGENTA}GENERAL EMPLOYEE DATA") 
    print("\n")

    questions = [
    inquirer.List(
        "Menu Options",
        message=f"{Fore.CYAN}Please select from the following options using the arrow keys, and press enter.",
        choices=["Display How Many Employee's Work for Initech", "Calculate Average Age of an Employee at Initech", "Calcaluate Average Salary of an Employee at Initech", "Return To Main Menu"],)]
    answers = inquirer.prompt(questions)
    
    if answers["Menu Options"] == "Display How Many Employee's Work for Initech":
        os.system('clear')
        display_number_of_employees()
    if answers["Menu Options"] == "Calculate Average Age of an Employee at Initech":
        os.system('clear')
        calculate_avg_age_of_employees()
    if answers["Menu Options"] == "Calcaluate Average Salary of an Employee at Initech":
        os.system('clear')
        calculate_avg_salary_of_employees()
    if answers["Menu Options"] == "Return To Main Menu":
       go_back_to_main_menu()   
    else:
        data_statistics_search()


def display_number_of_employees():
    """Function calculate's number of employees in employee_list."""
    i = 0
    try:
        for employee in employee_list:
            i = i + 1    
        print(f"{Fore.GREEN}The number of employee's currently employed at Initech is: {Fore.MAGENTA}'{i}'{Fore.GREEN}.\n")
        return i
    except TypeError:
        data_statistics_search()
        

def calculate_avg_age_of_employees():
    """Function calculate's the average age of employees in employee_list."""
    result = 0
    i = 0
    try: 
        for employee in employee_list:
            i = i + 1
            result = result + employee.age
        final_result = int(result / i)  
        print(f"{Fore.GREEN}The average age of an employee at Initech is: {Fore.MAGENTA}'{final_result}' {Fore.GREEN}years.\n")
        return final_result
    except TypeError:
        data_statistics_search()   


def calculate_avg_salary_of_employees():
    """Function calculate's the average salary of employees in employee_list."""
    result = 0
    i = 0
    try:
        for employee in employee_list:
            i = i + 1
            result = result + employee.salary    
        final_result = int(result / i)   
        print(f"{Fore.GREEN}The average salary of an employee at Initech is: {Fore.MAGENTA}'${final_result}' {Fore.GREEN}dollars.\n")
        return final_result
    except TypeError:
        data_statistics_search()



