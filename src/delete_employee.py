'''This allows for coloured text output in the terminal.'''
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

'''Import file for function employee_search to run'''
from employee_search import employee_search

'''Import file for access to employee_list'''
from employee import employee_list

'''Import file for functions to list_all_employees to run'''
from list_all_employees import list_all_employees

'''Function to delete a single employee from the database (employee_list)'''
def delete_employee():
    print(f"{Fore.BLUE}{Style.BRIGHT}\nDelete Employee:")
    employee = employee_search()
    if employee:
        employee_list.remove(employee)
    print(f"\n{Fore.GREEN}You have successfully deleted {Fore.MAGENTA}'{employee.name}'{Fore.GREEN} from the Employee Database:\n")    
    list_all_employees()
 