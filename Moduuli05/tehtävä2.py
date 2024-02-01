"""Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the program prints out the five greatest numbers sorted
in descending order. Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument."""

values =[]
while True:
    numbers = input("Enter a number: \n")

    if numbers == "":
        break

    values.append(int(numbers))

topFive = sorted(values,reverse=True)[:5]
print(topFive)