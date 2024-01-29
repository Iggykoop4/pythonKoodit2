# Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.
min_value = None
max_value = None

while True:
    user_input = input(f"give a number or use an empty string to quit\n")

    if user_input == '':
        print(f"Exiting")
        break

    number = int(user_input)

    if min_value is None or number < min_value:
        min_value = number
    if max_value is None or number > max_value:
        max_value = number


if min_value is not None and max_value is not None:
    print(f"min is {min_value}, max is {max_value}")
