'''Import file for access to employee_list and Employee Class.'''
from employee import Employee, employee_list

'''Allows user to create an entirely new instance of an employee and add it to the employee_list.'''
def create_employee():
    name = input("Please enter the employee's name:\n").title() 
    age = input("Please enter the employee's age:\n")
    role = input("Please enter the employee's role:\n").title()
    salary = input("Please enter the employee's salary:\n")
    employee_list.append(Employee(name, age, role, salary))