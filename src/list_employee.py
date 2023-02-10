'''This allows for coloured text output in the terminal.'''
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

'''A print-out of all employee attributes'''
def list_employee(employee):
    print(f"\n{Fore.CYAN}Name:{Fore.BLACK}{Style.BRIGHT} {employee.name}\n")
    print(f"{Fore.CYAN}Age:{Fore.BLACK}{Style.BRIGHT} {employee.age}\n")
    print(f"{Fore.CYAN}Role:{Fore.BLACK}{Style.BRIGHT} {employee.role}\n")
    print(f"{Fore.CYAN}Salary:{Fore.BLACK}{Style.BRIGHT} {employee.salary}\n")


