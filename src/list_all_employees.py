# This allows for shell commands in the terminal.
import os

# This import allows for the creation of a table.
from rich import print
from rich.console import Console
from rich.table import Table

# Need access to employee_list to print out table.
from employee import employee_list

# Allows the user to decide when to return to the main menu.
from return_main_menu import ask_return_main_menu


def list_all_employees():
    """Function that creates a table of all employees and their attributes."""
    table = Table(title="\n[bold magenta]Initech Employee Database[/bold magenta]\n", style="cyan")
    table.add_column("Name", style="green", justify="center")
    table.add_column("Age", style="blue", justify="center")
    table.add_column("Role", style="green", justify="center")
    table.add_column("Salary", style="blue", justify="center")
    for employee in employee_list:
        table.add_row(str(employee.name), str(employee.age), str(employee.role), str(employee.salary))
    print(table)
    
    ask_return_main_menu()
    
   

