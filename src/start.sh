#!/bin/bash

# CHECK IF PYTHON 3 IS INSTALLED
if ! [[ -x "$(command -v python3)" ]]
then
  echo "OOPS!: 
    This application needs Python 3 to be installed. For a MAC you can download
    it here: https://www.python.org/downloads/ " >&2
else
  echo "Good news you have Python Version 3" >&2
fi

# INSTALL NEEDED PACKAGES:

pip3 install inquirer

pip3 install rich

pip3 install colorama

pip3 install shutil

# WELCOME MESSAGE TO COLLECT INPUT FROM USER
echo "Hello there, to log in to the: 'Initech' Employee Database Application, please enter your name?"

read name

echo "It's nice to hear from you $name, you are now logged in to the: 'Initech' Employee Database Application."

# RUN APPLICATION COMMAND WITH ARGUMENT ENTERED:
python3 main.py $name

# PRINT OUT COPY OF TEXT FILE, ACCOUNT FOR ANY ERROR.
if [[ -e list_of_employees.txt ]]
then 
    echo "Print-out copy of: list_of_employees.txt:"
    cat list_of_employees.txt
else
    echo "Sorry, file: 'list_of_employees.txt' does not exist" >&2
fi   

echo "$name, you have successfully logged out the 'Initech' Employee Database Application. See you next time."
