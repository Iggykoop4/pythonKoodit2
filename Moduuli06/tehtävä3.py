"""Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
Write a main program that asks for a volume in gallons from the user and converts the value to liters.
The conversion must be done by using the function. Conversions continue until the user inputs a negative value."""


def gasoline():
    gallon_to_litre = 3.785
    while True:
        volume = float(input("How many gallons would you like to convert to litres?: "))
        if volume < 0:
            return

        liters = volume * gallon_to_litre
        print(f"your {volume} gallons in litres are : {liters} liters.")

gasoline()
