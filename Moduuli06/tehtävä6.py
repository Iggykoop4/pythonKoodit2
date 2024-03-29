"""Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros. The function calculates and returns the unit price of the pizza per square meter.
The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money (which of them has a lower unit price).
You must use the function you wrote for calculating the unit prices."""

def pizza_unit_price(diameter, price):
    radius = diameter / 2
    area = 3.14159 * (radius ** 2)
    unit_price = price / area
    return unit_price

diameter1 = float(input("Enter the diameter of the first pizza: "))
price1 = float(input("Enter the price of the first pizza: "))
unit_price1 = pizza_unit_price(diameter1, price1)

diameter2 = float(input("Enter the diameter of the second pizza: "))
price2 = float(input("Enter the price of the second pizza: "))
unit_price2 = pizza_unit_price(diameter2, price2)

if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")