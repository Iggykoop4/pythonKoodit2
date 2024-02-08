"""Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport, fetch the information of an existing airport or quit.
If the user chooses to enter a new airport, the program asks the user to enter the ICAO code and name of the airport.
If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport and prints out the corresponding name.
If the user chooses to quit, the program execution ends. The user can choose a new option as many times they want until they choose to quit.
 (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)"""

airports = {"Helsinki Vantaa": "EFHK",
            "Samoa Faleolo": "NSTU",
            "China Beijing": "ZBAA",
            "USA JFK": "KJFK"}

while True:
    found = False
    user_input = input("Please enter a new airport, fetch airport information or quit with empty string: ")
    user_input_low = user_input.lower()

    if user_input_low == "":
        print("Exiting")
        break
    for key, value in airports.items():
        if user_input_low == key.lower():
            print(f"The airport ICAO code is {value}")
            found = True
            break
        elif user_input_low == value.lower():
            print(f"The airport name is {key}")
            found = True
            break
    if not found:
        new_air = input("Airport does not exist in database, please enter airport name to add: ").capitalize()
        new_ICAO = input("Airport ICAO number: ").upper()
        airports.update({new_air: new_ICAO})
