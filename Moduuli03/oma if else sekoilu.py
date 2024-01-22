raha = 5
latte = 7
poor = True
print(f"Sinulla on {raha} ja latte maksaa {latte}")
if raha > 7:
    poor = False
    print("voit ostaa latten")
else:
    poor == True
print("Olet köyhä")

if poor == True:
    raha = raha + 5
    poor = False
    print(f"sait lisää rahaa: {raha}")
    print("voit ostaa latten")
    raha = raha - latte
    print(f"Ostat laten ja sinulle jää {raha - latte} rahaa")

    poor = True
