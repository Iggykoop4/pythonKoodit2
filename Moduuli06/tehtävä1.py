#Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters.
#Write a main program that rolls the dice until the result is 6. The main program should print out the result of each roll.

import random


def dice():
    while True:
        roll = random.randint(1, 6)
        print(f"You rolled: {roll}")
        if roll == 6:
            return

dice()