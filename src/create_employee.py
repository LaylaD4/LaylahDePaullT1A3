'''Import file for access to employee_list and Employee Class.'''
from employee import Employee, employee_list

'''Import file for functions; check_for_valid_string & check_for_valid_number to run'''
from check_inputs import check_for_valid_string, check_for_valid_number

'''Allows user to create an entirely new instance of an employee and add it to the employee_list.'''
def create_employee():
    name = check_for_valid_string("Please enter the employee's name:\n").title() 
    age = check_for_valid_number("Please enter the employee's age:\n")
    role = check_for_valid_string("Please enter the employee's role:\n").title()
    salary = check_for_valid_number("Please enter the employee's salary:\n")
    employee_list.append(Employee(name, age, role, salary))