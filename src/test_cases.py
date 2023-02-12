'''Imported to run testing.'''
import pytest

'''Imported to add input'''
import builtins

from pytest import MonkeyPatch

'''Import file for access to Employee Class, and employlee_list.'''
from employee import Employee, employee_list

'''Imported to run tests on feature: calculate_avg_age_of_employees '''
from data_statistics_search import calculate_avg_age_of_employees

'''Imported to run tests on feature: check_for_valid_number'''
from check_inputs import check_for_valid_number


# FIRST FEATURE TEST --> calculate_avg_age_of_employees(). This feature calculates the average
# age of employees listed in the employee database (employee_list). 

def test_calculate_avg_age_of_employees():
    # 1) Test Case: check calculate_avg_age_of_employee function is working correctly
    # by adding another instance of an Employee to the employee_list (database). Currently
    # the average age of an employee is : 27 years (139/5)
    
    # Append a new employee to the employee_list who has an age = 45
    employee_list.append(Employee("Peter Piper", 45, "Management", 120000))

    # Set local variable to equal function to be tested."
    avg_age = calculate_avg_age_of_employees()

    # With the addition of employee: "Peter Piper" at age = 45 increases sum total of ages to: 184 (139 + 45)
    # Now when divided by the total number of employees, now: 6, ie; 184/6 == 30  (function returns integer - base 10)
    assert avg_age == 30
    #    assert 30 == 30 
    # Therefore: calculate_avg_age_of_employees() function working as expected in this test case.

    # 2) Test Case: check calculate_avg_age_of_employee function is working correctly by removing an 
    # instance of an employee from the database (employee_list).

    # Retrieving employee that is to be removed from the: employee_list.
    for employee in employee_list:
        if employee.name == "Omar Turan":
            # Removing employee instance: "Omar Turan" who's age = 35 years from the employee_list.
            employee_list.remove(employee)

    # Set local variable to equal function to be tested."
    avg_age = calculate_avg_age_of_employees()

    # With the removal of employee "Omar Turan" at age = 35 decreases sum total of ages to: 149 (184 - 35)
    # Now when divided by the total employees of now: 5, ie; 149/5 == 29 (function returns integer - base 10)
    assert avg_age == 29
    #    assert 29 == 29 
    # Therefore: calculate_avg_age_of_employees() function working as expected in this test case.



# SECOND FEATURE TEST --> check_for_valid_number(message). This feature takes in any string input from
# a user, handles (error logic) for all inputs types: letters/numbers/symbols, converts a valid input 
# (number character) to an integer, and in the case of an "age" argument input; which I am checking 
# here; checks that it is >= 18.

def test_check_for_valid_number(monkeypatch):
    # 1) Test Case: check that the feature: 'check_for_valid_number' is working correctly by entering in 
    # a variety of different entries that will be iterated through until a valid one is found. That is; 
    # an entry that is made up of only numbered characters, and is >=18.

    # Create the 'inputs' variable that's contents are to be iterated through until a valid entry is found:
    inputs = iter(["12", "Hello World!", "17.99", "25", "30"])
    
    # Because the feature asks for user input, need to enter that input using monkeypatch import.
    monkeypatch.setattr('builtins.input', lambda _: next(inputs)) 
    
    # Set local variable to equal function to be tested."
    number = check_for_valid_number("Please enter the employee's age:\n", "age")  
    
    # Using monkeypatch; the 'inputs' variable storing the various entries is
    # iterated through until a valid entry is found. That is; an entry that is 
    # made up of solely numbered characters (can be converted to an integer), and is >= 18.
    # Here, the first valid entry seen in the iteration is: "25", therefore the feature returns: 25.
    assert number == 25
    #   assert 25 == 25    - Therefore: check_for_valid_number() function working as expected.


    # 2) Test Case: check that the feature: check_for_valid_number is working correctly by entering 
    # various string entries to be iterated through, the feature then correctly selects the first valid 
    # entry of: "18.525" even though it is a decimal number, handles entry, and is able to convert it 
    # to an integer type. 

    # Create the 'inputs' variable that's contents are to be iterated through until a valid entry is found:
    inputs = iter(["-12.5", "18.525", "51"])

    # Because the feature asks for user input, need to enter that input using monkeypatch.
    monkeypatch.setattr('builtins.input', lambda _: next(inputs)) 

    # Set local variable to equal function to be tested."
    number = check_for_valid_number("Please enter the employee's age:\n", "age")

    # Using monkeypatch; the 'inputs' variable storing the various entries is
    # iterated through until a valid entry is found, in this case it correctly selects: "18.525", 
    # handles decimal entry, and converts the entry to the desired object type of 'int' (integer).
    assert number == 18
    #   assert 18 == 18   - Therefore: check_for_valid_number() function working as expected.
    assert type(number) == int
    #        assert int == int   - Therefore: check_for_valid_number() function working as expected.

