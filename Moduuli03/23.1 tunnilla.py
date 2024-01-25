#while silmukat (loopit)

#jakolaskukone , jakaja ei voi olla nolla
""" monen rivin merkkijono, käytetään myös monen rivin kommentoimiseen.
num1 = float(input("anna jaettava "))
num2 = float(input("anna jakaja"))
while num2 == 0:
    print("Ei voi olla nolla")
    num2 = float(input("Anna jakaja"))
result = num1 / num2
print(f"jakolaskun tulos on: {result}")
"""
#iteroiva silmukka (käytetään  "laskuria" silmukan toistokertojen määrittelyyn.)

#i = 1 #iteraattori 1
"""
i = int(input("mistä numerosta aloitetaan?"))
amount = int(input("Kuinka monta numeroa tulostetaan?"))
offset = int(input("Anna numero väli: "))
max_number = amount * offset + i

while i <=max_number:  # AIna True tai False arvo
    print(f"Numero on {i}")
    i = i + offset
print(f"i:n lopullinen arvo {i}") #11

#voit testata ehtolauseen toimintaaa tulostamalla niiden arvoja
print(i < i+1)   # -> True
"""

import random

random_number = random.randint(1,3)
print(f"Random number: {random_number}")

player_count = 2
current_player = 1
dice_amount = 3

# jokainen pelaaja suorittaa vuorollaan
while current_player <= player_count:
    result = 0 # nopan silmälukujen summa ennen heittoja
    throw_count = 0
    while throw_count < dice_amount:
        die = random.randint(1, 6)
        print(f"Pelaaja {current_player} {throw_count}. heitto: {die}")
        result = result + die
        throw_count += 1 # sama kuin throw_count = throw_count +1
    print(f"Pelaajan {current_player} tulos  {result}")
    current_player = current_player + 1
