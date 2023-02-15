# This allows for coloured text output in the terminal.
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def list_employee(employee):
    """A print-out of all employee attributes.
    
    :param employee: an Employee instance.
    """
    print(f"\n{Fore.CYAN}Name:{Fore.GREEN}{Style.BRIGHT} {employee.name}\n")
    print(f"{Fore.CYAN}Age:{Fore.BLUE}{Style.BRIGHT} {employee.age}\n")
    print(f"{Fore.CYAN}Role:{Fore.GREEN}{Style.BRIGHT} {employee.role}\n")
    print(f"{Fore.CYAN}Salary:{Fore.BLUE}{Style.BRIGHT} {employee.salary}\n")


