#!/bin/bash

# CHECK IF PYTHON 3 IS INSTALLED
if ! [[ -x "$(command -v python3)" ]]
then
  echo "OOPS!: 
    This application needs Python 3 to be installed. For a MAC you can download
    it here: https://www.python.org/downloads/ " >&2
    exit
else
  echo "Good news you have Python Version 3" >&2
fi

# INSTALL NEEDED PACKAGES:

if [[ -x "$(command -v pip3)" ]]
then
  pip3 install inquirer

  pip3 install rich

  pip3 install colorama

  pip3 install shutil
  
else
  sudo pip3 install inquirer --user

  sudo pip3 install rich --user

  sudo pip3 install colorama --user

  sudo pip3 install shutil --user
fi



# WELCOME MESSAGE TO COLLECT INPUT FROM USER

#Set the prompt for user input
echo -e "Hello there, to log in to the: 'Initech' Employee Database Application, please enter your name?"

# Initialize the name variable
name=""

# Start the while loop
while [ -z "$name" ]; do
  # Read the user input
  read name

  # Check if the name is blank
  if [ -z "$name" ]; then
    echo "You did not enter your name. Please try again."
    echo -e "Hello again! To log in to the: 'Initech' Employee Database Application, please enter your name? "
  fi
done

# change name variable to be capital case using the awk command.
name="$(echo $name | awk '{for (i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) substr($i,2)} 1')"

echo "It's nice to hear from you $name, you are now logged in to the: 'Initech' Employee Database Application."

# RUN APPLICATION COMMAND WITH ARGUMENT ENTERED:
python3 src/main.py $name

# PRINT OUT COPY OF TEXT FILE, ACCOUNT FOR ANY ERROR WHEN USER EXITS APP.
if [[ -e list_of_employees.txt ]]
then 
    echo "Print-out copy of: list_of_employees.txt:"
    cat list_of_employees.txt
else
    echo "Sorry, file: 'list_of_employees.txt' does not exist" >&2
fi   

# FINAL MESSAGE AFTER APP EXITED:
echo "$name, you have successfully logged out of the 'Initech' Employee Database Application. See you next time."
