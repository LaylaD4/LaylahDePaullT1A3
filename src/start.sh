#!/bin/bash

# Check If Python 3 is installed.
if ! [[ -x "$(command -v python3)" ]]
then
  echo "OOPS!: 
    This application needs Python 3 to be installed. For a MAC you can download
    it here: https://www.python.org/downloads/ " >&2
    exit
else
  echo "Good news you have Python Version 3" >&2
fi

# Install dependancies.
if [[ -x "$(command -v pip3)" ]]
then
  pip3 install inquirer

  pip3 install rich

  pip3 install colorama

  pip3 install shutil
  
else
  echo "OOPS!: 
    If you receive an [Errono 13] - 'Could not install packages due to an Environment:Error'. Please
    refer to the Help Documentation in README for instructions to install python packages individually." >&2
    exit
fi

# Clear terminal.
clear


# Welcome message to prompt for user input.
echo -e "Hello there, to log in to the: 'Initech' Employee Database Application, please enter your name?"

# Initialize the name variable to store user input.
name=""

# While loop to ensure user adds input of their name:
while [ -z "$name" ]; do
  # Read the user input
  read name

  # Check if the name is blank
  if [ -z "$name" ]; then
    echo "You did not enter your name. Please try again."
    echo -e "Hello again! To log in to the: 'Initech' Employee Database Application, please enter your name? "
  fi
done

# Change name variable input to be capital case using the awk command.
name="$(echo $name | awk '{for (i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) substr($i,2)} 1')"

echo "It's nice to hear from you $name, you are now logged in to the: 'Initech' Employee Database Application."


# Run python script (application) command with argument of user's input.
python3 src/main.py $name

# Print out copy of text file, account for any error when user exits application.
if [[ -e list_of_employees.txt ]]
then 
    echo "Print-out copy of: list_of_employees.txt:"
    cat list_of_employees.txt
else
    echo "Sorry, file: 'list_of_employees.txt' does not exist" >&2
fi   

# Final message to user in terminal after application exited.
echo "$name, you have successfully logged out of the 'Initech' Employee Database Application. See you next time."
