# Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
#radius = float(input("What's your circle radius?\n"))
#pii = 3.141592653589793
#new_area = ((pii) * (radius) * (radius))
#print("Your circle Area is: ", new_area)

import math
radius = float(input("Your radius?"))
new_area = (math.pi * radius**2)
print(f"The area of your circle is:\n{new_area:.2f}")