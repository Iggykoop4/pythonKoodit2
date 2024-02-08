while True:
    print(f"Hello, please enter your cabin class\nLUX\nA\nB\nC\n")
    user_choice = input("Which Cabin class you have? :").upper()
    if user_choice == "LUX":
        print(f"You have upper-deck cabin with a balcony\n")
        break
    elif user_choice == "A":
        print(f"Your cabin is above the car deck, equipped with a window.\n")
        break
    elif user_choice == "B":
        print(f"Your cabin is windowless cabin above the car deck.\n")
        break
    elif user_choice == "C":
        print(f"Your cabin is windowless cabin below the car deck.\n")
        break
    else:
        print("Invalid cabin class, please choose a valid option: LUX, A, B or C \n")

