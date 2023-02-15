# This import allows for coloured text output in the terminal.
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Import file for access to employee_list and Employee Class.
from employee import Employee, employee_list

# Import file for functions; check_for_valid_string & check_for_valid_number to run.
from check_inputs import check_for_valid_string, check_for_valid_number

# Import file for function list_employees to run.
from list_employee import list_employee

# Allows the user to return to the main menu.
from return_main_menu import ask_return_main_menu


def create_employee():
    """Function allows user to create an entirely new instance of an employee and add it to employee_list."""
    print(f"\n{Fore.BLUE}{Style.BRIGHT}Create Employee:\n")
    name = check_for_valid_string(f"\n{Fore.CYAN}Please enter the employee's name:{Fore.BLACK}\n").title() 
    age = check_for_valid_number(f"\n{Fore.CYAN}Please enter the employee's age:{Fore.BLACK}\n", "age")
    role = check_for_valid_string(f"\n{Fore.CYAN}Please enter the employee's role:{Fore.BLACK}\n").title()
    salary = check_for_valid_number(f"\n{Fore.CYAN}Please enter the employee's salary:{Fore.BLACK}\n", "salary")
    employee_list.append(Employee(name, age, role, salary))

    # Return instance of employee just created.
    for employee in employee_list:
        if employee == name:
            return employee

    # Confirm to the user the employee instance was created.
    print(f"\n{Fore.MAGENTA}You have successfully added {Fore.CYAN}'{employee.name}'{Fore.MAGENTA} to the Employee Database.\n")
    
    list_employee(employee) 

    ask_return_main_menu()       