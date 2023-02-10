'''Import file for function employee_search to run'''
from employee_search import employee_search

'''Import file for functions; check_for_valid_string & check_for_valid_number to run'''
from check_inputs import check_for_valid_string, check_for_valid_number, only_letters, handle_number_errors

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
            if only_letters(new_name) == False:
                raise ValueError("Please re-enter the correct new name of the employee:\n")
            else:
                new_name
        except ValueError as warning:
            new_name = check_for_valid_string(warning).title()
    # Check for a valid number if input given.
    new_age = input("Please type new age, or press enter to skip \n")
    if new_age != "":
        try:
            new_age = int(float(new_age))
            if new_age >= 18:
                new_age = handle_number_errors(new_age, "age")
            else:
                new_age = new_age = check_for_valid_number("Please re-enter the age. Remember it must be a number, and be 18 or above:\n", "age")
        except ValueError:
            new_age = check_for_valid_number("Please re-enter the age. Remember it must be a number, and be 18 or above:\n", "age")  
    # Check for a valid string if input given.
    new_role = input("Please type new role, or press enter to skip \n").title()
    if new_role != "":
        try:
            if only_letters(new_role) == False:
                raise ValueError("Please re-enter the correct new role of the employee:\n")
            else:
                new_role
        except ValueError as warning:
            new_role = check_for_valid_string(warning).title()
    # Check for a valid number if input given.
    new_salary = input("Please type new salary, or press enter to skip \n")
    if new_salary != "":
        try:
            new_salary = int(float(new_salary))
            if new_salary >= 42000:
                new_salary = handle_number_errors(new_salary, "salary")
            else:
                new_salary = check_for_valid_number("Please re-enter the salary. Remember it must be a number equal to or above 42000:\n", "salary")
        except ValueError:
            new_salary = check_for_valid_number("Please re-enter the salary. Remember it must be a number equal to or above 42000:\n", "salary")  
   
    '''If a new name, age, role, or salary is entered change it to new_name/age/role/salary.'''
    if new_name != "":
        employee.name = new_name
    if new_age != "":
        employee.age = new_age
    if new_role != "":
        employee.role = new_role
    if new_salary != "":
        employee.salary = new_salary
    print(f"\nYour newly edited employee: '{employee.name}' is listed below:\n")
    list_employee(employee)
    edit_employee()
    ask_return_main_menu()
    