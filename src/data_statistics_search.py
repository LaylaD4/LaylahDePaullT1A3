'''Import file for access to employee_list'''
from employee import employee_list

'''Allows user to select menu option.'''
def data_statistics_search():
    pass

'''Function to calculate number of employees in database (employee_list).'''
def display_number_of_employees():
    i = 0
    try:
        for employee in employee_list:
            i = i + 1    
        print(f"The number of employee's currently employed at Initech is: '{i}'.\n")
        #data_statistics_search()
        return i
    except TypeError:
        data_statistics_search()

'''Function to calculate the average age of employees in the database (employee_list).'''
def calculate_avg_age_of_employees():
    result = 0
    i = 0
    try: 
        for employee in employee_list:
            i = i + 1
            result = result + employee.age
        final_result = int(result / i)  
        print(f"The average age of an employee at Initech is: '{final_result}' years.\n")
        #data_statistics_search()
        return final_result
    except TypeError:
        data_statistics_search()   

'''Function to calculate the average salary of employees in the database (employee_list).'''
def calculate_avg_salary_of_employees():
    result = 0
    i = 0
    try:
        for employee in employee_list:
            i = i + 1
            result = result + employee.salary    
        final_result = int(result / i)   
        print(f"The average salary of an employee at Initech is: '${final_result}' dollars.\n")
        #data_statistics_search()
        return final_result
    except TypeError:
        data_statistics_search()

