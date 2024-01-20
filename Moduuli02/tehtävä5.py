lot = 0.0133
pound = lot * 32
talent = pound * 20
lots = float(input("give lots: \n"))
pounds = float(input("give pounds: \n"))
talents = float(input("give talents: \n"))
kilot = ((lot * lots) + (pound * pounds) + (talent * talents))

fullKilo = int(kilot)
grams = kilot % 1 * 1000
print(f"{fullKilo} Kiloa ja {grams:.0f} grammaa.")
