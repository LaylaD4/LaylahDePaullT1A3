'''To search for an employee need to import the list of Employee instances.'''
from employee import employee_list

'''Allows the user to decide when to return to the main menu.'''
from return_main_menu import ask_return_main_menu

'''Import datetime module to get current date.'''
from datetime import date

'''Import system() method to allows you to execute the cat shell script in python file.'''
import os

'''Centres output in terminal'''
from print_centre import print_centre

def print_employee_list():
    print("\n")
    print_centre("PRINT EMPLOYEE LIST TO FILE")
    print("\n")
    text_file = open("list_of_employees.txt", "w")
    num = 0
    today = date.today()
    text_file.write("Initech Employee Database\n")
    text_file.write(f"Date Printed: {str(today)} \n\n")
    for employee in employee_list:
        num += 1
        entry = f"Employee {num}:\n Name: {employee.name}\n Age: {employee.age}\n Role: {employee.role}\n Salary: {employee.salary} \n\n"
        text_file.write(entry)
    text_file.close()
    print_centre("Congratulations; your 'Initech Employee Database' list has now been printed successfully to the file: 'list_of_employees.txt'. Below is a copy of what is printed in that text file:\n") 
    os.system("cat list_of_employees.txt")
    ask_return_main_menu()
