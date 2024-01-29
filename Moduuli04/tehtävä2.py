cm = 2.54
inch = float(input("input inches:\n"))
while inch > 0:
    result = inch * cm
    print(f"{result:.2f} centimetres.")
    inch = float(input("Give new inch amount"))
    if inch < 0:
        print(f"Can't have negative inches!")
        break