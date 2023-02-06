'''This allows for the creation of a table that includes all employees and their attributes in it.'''
from rich import print
from rich.console import Console
from rich.table import Table

'''Need access to employee_list to print out table.'''
from employee import employee_list

'''Allows the user to decide when to return to the main menu.'''
from return_main_menu import ask_return_main_menu


'''Function that creates a Table of the employees and their attributes.'''
def list_all_employees():
    table = Table(title="\n[bold magenta]Initech Employee Database[/bold magenta]\n", style="cyan")
    table.add_column("Name", style="cyan", justify="center")
    table.add_column("Age", justify="center")
    table.add_column("Role",justify="center")
    table.add_column("Salary", justify="center")
    for employee in employee_list:
        table.add_row(str(employee.name), str(employee.age), str(employee.role), str(employee.salary))
        
    print(table)
    
    ask_return_main_menu()
   