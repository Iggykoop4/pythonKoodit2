while True:
    gender = str(input(f"Are you male or female?")).upper()
    hemoglobin = int(input(f"What's your hemoglobin value?"))
    if gender == "MALE":
        if hemoglobin < 134:
            print("Hemoglobin is too low!")
            break
        elif 134 <= hemoglobin <= 167:
            print("Hemoglobin is okay")
            break
        elif hemoglobin > 167:
            print("Hemoglobin is too high!")
            break
    elif gender == "FEMALE":
        if hemoglobin < 117:
            print("Hemoglobin is too low!")
            break
        elif 117 <= hemoglobin <= 155:
            print("Hemoglobin is okay")
            break
        elif hemoglobin > 155:
            print("Hemoglobin is too high!")
            break
    else:
        print("Invalid gender")