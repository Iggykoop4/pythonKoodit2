# Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome.
# After five failed attempts the program prints out Access denied. The correct username is python and password rules.

user_inputName = input(f"Enter username:\n")
user_inputPass = input(f"Enter password:\n")
username = "Kassi"
password = "Alma"
attempt_number = 0

while user_inputName != username or user_inputPass != password and attempt_number > 5:
    print("Wrong username or password\n")
    user_inputName = input(f"Enter username:\n")
    user_inputPass = input(f"Enter password:\n")
    attempt_number = attempt_number + 1
    if attempt_number == 5:
        print("You have reached the limit of tries")
        break

if user_inputName == username and user_inputPass == password: print("Welcome")