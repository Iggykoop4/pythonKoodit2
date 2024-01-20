import random

# Generate 9 random digits as a string
random_digits9_1 = ''.join(random.choice('0123456789') for _ in range(9))
random_digits9_2 = ''.join(random.choice('0123456789') for _ in range(9))
random_digits4_1 = ''.join(random.choice('0123456789') for _ in range(4))
random_digits4_2 = ''.join(random.choice('0123456789') for _ in range(4))
print(f"Random 9 digits: {random_digits9_1}\nRandom 9 digits: {random_digits9_2}")
print(f"Random 4 digits: {random_digits4_1}\nRandom 4 digits: {random_digits4_2}")