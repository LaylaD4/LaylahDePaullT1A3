'''This allows for a list function output for user to scroll up & down through.'''
import inquirer

'''To search for an employee need to import the list of Employee instances.'''
from employee import employee_list

'''Allows the user to return to the main menu.'''
from return_main_menu import go_back_to_main_menu

'''Create a way for user to search employee of interest by name.'''
def employee_search():
    employee_names = []
    for employee in employee_list:
        employee_names.append(employee.name)
    
    print("\n")
    print("LIST OF EMPLOYEES") 
    print("\n")

    questions = [
    inquirer.List(
        "Employees",
        message="Please select an employee from the list using the arrow keys, and then press enter.",
        choices= employee_names + ["Return to Main Menu"],)]
    selection = inquirer.prompt(questions)
    
    for name in employee_names:
        if selection["Employees"] == name:
            # Search through employee list:
            for employee in employee_list:
                # Check if employee name matches employee list name:
                if name == employee.name:
                    return employee
        if selection["Employees"] == "Return to Main Menu":
            go_back_to_main_menu()
            