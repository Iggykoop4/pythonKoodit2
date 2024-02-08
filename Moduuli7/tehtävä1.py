"""Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program.
We can define each season to last three months, December being the first month of winter."""

seasons = ("Spring", "Summer", "autumn", "winter")
month = int(input("Give me an integer between 1 and 12: "))
if 1 <= month <= 12:
    if 3 <= month <= 5:
        season = seasons[0]
    elif 6 <= month <= 8:
        season = seasons[1]
    elif 9 <= month <= 11:
        season = seasons[2]
    else:
        season = seasons[3]

print(f"The season is {season}.")
