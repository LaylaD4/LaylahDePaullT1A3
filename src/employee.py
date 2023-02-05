'''Create an Employee class to create an instance of an employee'''
class Employee:
    def __init__(self, name, age, role, salary):
        self.name = name
        self.age = age
        self.role = role
        self.salary = salary

'''This is the 'Employee Database', that is; a list that stores all instances of an employee.'''
employee_list = [Employee("Luke Smith", 20, "Developer", 100000), Employee("Hannah Norton", 25, "Graphic Design", 80000), Employee("Eric Wilson", 34, "Management", 120000), Employee("Elise Sorensen", 25, "Developer", 100000), Employee("Omar Turan", 35, "Sales", 120000),]
