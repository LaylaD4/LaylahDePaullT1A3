'''To search for an employee need to import the list of Employee instances.'''
from employee import employee_list

'''Allows the user to decide when to return to the main menu.'''
from return_main_menu import ask_return_main_menu

def print_employee_list():
    print("\n")
    print("PRINT EMPLOYEE LIST TO FILE")
    print("\n")
    text_file = open("list_of_employees.txt", "w")
    num = 0
    text_file.write("Initech Employee Database\n\n")
    for employee in employee_list:
        num += 1
        entry = f"Employee {num}:\n Name: {employee.name}\n Age: {employee.age}\n Role: {employee.role}\n Salary: {employee.salary} \n\n"
        text_file.write(entry)
    text_file.close()
    print("Congratulations; your 'Initech Employee Database' list has now been printed successfully to the file: 'list_of_employees.txt'.\n") 
    ask_return_main_menu()
    
   