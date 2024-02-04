"""Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed.
 For testing, write a main program where you create a list, call the function, and then print out both the original as well as the cut-down list."""


def uneven_numbers(items):
    even_numbers = [item for item in items if item % 2 == 0]
    return even_numbers


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list: {numbers_list}")

even_numbers = uneven_numbers(numbers_list)

print(f"even numbers: {even_numbers}")
