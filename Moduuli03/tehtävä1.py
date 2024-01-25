zander = input("How long is your Zander?: ")
min_zander = 42
zander_small = (min_zander - int(zander))
if int(zander) < min_zander:
    print(f"Your Zander is {zander_small} centimeters too small, you can't keep it.")
else:
    print(f"You can keep your zander")