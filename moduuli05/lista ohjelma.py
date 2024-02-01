items = [1,3,4,5,6,9,10,17,23,24]
parittomat = []
for item in items:
    if item % 2 != 0:
        (parittomat.append(item))

print(parittomat)