# muuttuja Variable ja tyyppi

age = 5
print(age)
age = 6
print(age)
age = 7
print(age)
# merkkijono
age_string = "seitsemän"
# kokonaisluku
age_int = 6

# ei toimi: print(age_string + age_int)

print (age_int +4)
# merkkijonojen liittäminen (concatenation)
print (age_string + " vuotta")

# liukuluvut (float) (ei ihan sama(tarkka) kuin desimaaliluku)
#7000 = 7_000
depth = 10.3
width = 7
area = depth * width
print(area)

#boolean: totta vai tarua (pythonissa 1 tai 0) muista iso Alkukirjain True ja False
is_It_True = True
print(is_It_True)

#tyyppimuutokset
age_Input = input("kuinka vanha olet?")
#print(type(ageInput)) # "13"
age_int = int(age_Input)
new_age = age_int + 1
print("vuoden päästä olet " + str(new_age) + " vuotta.")
#tai "f-stringillä"
print(f"vuoden päästä olet {new_age} vuotta.")