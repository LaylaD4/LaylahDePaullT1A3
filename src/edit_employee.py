'''Import file for function employee_search to run'''
from employee_search import employee_search

'''Import file for functions; check_for_valid_string & check_for_valid_number to run'''
from check_inputs import check_for_valid_string, check_for_valid_number

'''Import file for function list_employees to run'''
from list_employee import list_employee

'''Allows the user to return to the main menu.'''
from return_main_menu import ask_return_main_menu

def edit_employee(): 
    print("Edit Employee:\n")
    employee_exists = employee_search()
    if employee_exists:
        edit_employee_attributes(employee_exists)

'''Allows user to edit the attributes of the chosen employee.'''
def edit_employee_attributes(employee):
    # Check for a valid string if input given.
    new_name = input("Please type new name, or press enter to skip \n").title()
    if new_name != "":
        try:
            if new_name.isdigit():
                raise ValueError("Please re-enter the correct new name of the employee:\n")
            else:
                new_name
        except ValueError as warning:
            new_name = check_for_valid_string(warning).title()
    # Check for a valid number if input given.
    new_age = input("Please type new age, or press enter to skip \n")
    if new_age != "":
        try:
            new_age = int(new_age)
        except ValueError:
            new_age = check_for_valid_number("Please re-enter the age. Remember it must be a number:\n")  
    # Check for a valid string if input given.
    new_role = input("Please type new role, or press enter to skip \n").title()
    if new_role != "":
        try:
            if new_role.isdigit():
                raise ValueError("Please re-enter the correct new role of the employee:\n")
            else:
                new_role
        except ValueError as warning:
            new_role = check_for_valid_string(warning).title()
    # Check for a valid number if input given.
    new_salary = input("Please type new salary, or press enter to skip \n")
    if new_salary != "":
        try:
            new_salary = int(new_salary)
        except ValueError:
            new_salary = check_for_valid_number("Please re-enter the salary. Remember it must be a number:\n") 
   
    '''If a new name, age, role, or salary is entered change it to new_name/age/role/salary.'''
    if new_name != "":
        employee.name = new_name
    if new_age != "":
        employee.age = new_age
    if new_role != "":
        employee.role = new_role
    if new_salary != "":
        employee.salary = new_salary
    print("\nYour newly edited employee: '{employee.name}' is listed below:\n")
    list_employee(employee)
    edit_employee()
    ask_return_main_menu()
    