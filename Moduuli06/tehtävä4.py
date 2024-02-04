"""Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the list.
For testing, write a main program where you create a list, call the function, and print out the value it returned."""
def sum_laskuri (items):
    summa = sum(items)
    print(f"Sum of all numbers in the list: {summa}")
    return summa


numerot = [0,10,20,40,30,1,1,8]
sum_laskuri(numerot)
