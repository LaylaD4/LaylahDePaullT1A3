'''This allows for a list function output for user to scroll up & down through.'''
import inquirer

'''Import file for access to employee_list'''
from employee import employee_list

'''Allows the user to return to the main menu.'''
from return_main_menu import go_back_to_main_menu

'''Centres output in terminal'''
from print_centre import print_centre

'''Allows user to select menu option.'''
def data_statistics_search():
    print("\n")
    print_centre("GENERAL EMPLOYEE DATA") 
    print("\n")

    questions = [
    inquirer.List(
        "Menu Options",
        message="Please select from the following options using the arrow keys, and press enter.",
        choices=["Display How Many Employee's Work for Initech", "Calculate Average Age of an Employee at Initech", "Calcaluate Average Salary of an Employee at Initech", "Return To Main Menu"],)]
    answers = inquirer.prompt(questions)
    
    if answers["Menu Options"] == "Display How Many Employee's Work for Initech":
        display_number_of_employees()
    if answers["Menu Options"] == "Calculate Average Age of an Employee at Initech":
        calculate_avg_age_of_employees()
    if answers["Menu Options"] == "Calcaluate Average Salary of an Employee at Initech":
       calculate_avg_salary_of_employees()
    if answers["Menu Options"] == "Return To Main Menu":
       go_back_to_main_menu()   
    else:
        data_statistics_search()

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



