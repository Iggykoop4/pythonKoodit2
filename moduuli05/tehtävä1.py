#Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.
import random
dices = int(input("How many dice you want to throw?:\n"))
print("Rolling")
for i in range(dices):
    roll = random.randint(1,6)
    i = i + 1
    print(roll)