#Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until
# they guess the right number. After each guess the program prints out a text:
# Too high, Too low or Correct. Notice that the computer must not change the number between guesses.
import random

guess_counter = 0
computer = random.randint(1, 10)
player = int(input("Enter a number between 1 and 10:\n"))
guess_counter = guess_counter + 1
while player < 1 or player > 10:
    print("Invalid number")
    guess_counter = 0
    player = int(input("Enter a number between 1 and 10:\n"))
    guess_counter = guess_counter + 1

while computer != player:
    if computer < player:
        print("Too high")
    elif computer > player:
        print("Too low")
    player = int(input("Make a new guess 1 and 10:\n"))
    guess_counter = guess_counter + 1
    if player < 1 or player > 10:
        print("Invalid number")
    if computer == player:
        print(f"Congratulations, you guessed correctly in {guess_counter} tries!")
        break
