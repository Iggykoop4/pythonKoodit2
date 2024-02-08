"""Write a program that asks the user to enter names until he/she enters an empty string.
After each name is read the program either prints out New name or Existing name depending on whether the name was entered for the first time.
Finally, the program lists out the input names one by one, one below another in any order. Use the set data structure to store the names."""

names = set()
while True:
    name = input("Enter name, empty string quits:")

    if name == '':
        break

    if name not in names:
        print(f"{name} added to the list.")
    else:
        print(f"{name} already in the list")
    names.add(name)

for i in names:
    print(f"{i}\n")
