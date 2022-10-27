def calc_price():
    # Loop, um Eingabe bis zur erfolgreichen Eingabe zu wiederholen
    finished = False
    while not finished:
        gender = ("1" == input("Männlich (1) oder Weiblich (0): "))
        age = input("Dein Alter: ").strip().replace(",", ".")

        if age.isdigit():
            age = int(age)
        else:
            print("Das ist keine Zahl!\n")
            continue

        dyeing = ("1" == input("Möchtest du dein Haar färben? 1 für ja, 0 für nein: "))
        drying = ("1" == input("Möchtest du dein Haar trocknen? 1 für ja, 0 für nein: "))

        # Den Preis für die Person herausfinden
        if gender:
            if age <= 14:
                total = 10
            else:
                total = 15
        else:
            if age <= 16:
                total = 12
            else:
                total = 20

        # AddOns zum Preis dazu
        if dyeing: total += 10
        if drying: total += 5

        # End loop
        finished = True
        return total

print("Der Preis für deinen Friseurbesuch beträgt {:.2f}€".format(calc_price()))
