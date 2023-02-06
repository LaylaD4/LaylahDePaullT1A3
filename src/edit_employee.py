'''Import file for function employee_search to run'''
from employee_search import employee_search

def edit_employee(): 
    print("Edit Employee:\n")
    employee_exists = employee_search()
    if employee_exists:
        edit_employee_attributes(employee_exists)

'''Allows user to edit the attributes of the chosen employee.'''
def edit_employee_attributes(employee):
    pass