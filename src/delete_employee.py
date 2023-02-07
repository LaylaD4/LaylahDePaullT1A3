'''Import file for function employee_search to run'''
from employee_search import employee_search

'''Import file for access to employee_list'''
from employee import employee_list

'''Import file for functions to list_all_employees to run'''
from list_all_employees import list_all_employees

'''Function to delete a single employee from the database (employee_list)'''
def delete_employee():
    employee = employee_search()
    if employee:
        employee_list.remove(employee)
    print(f"\nYou have successfully deleted '{employee.name}' from the Employee Database:\n")    
    list_all_employees()
 