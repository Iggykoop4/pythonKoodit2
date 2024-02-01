

probabilities = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6,0.7,0.8,0.9]
newList = []
for prob in probabilities:
    if prob <= 0.5:
        prob = 0
        newList.append(prob)
    if prob > 0.5:
        prob = 1
        newList.append(prob)


print(newList)
pituus = len(newList) #len = length
print(pituus)