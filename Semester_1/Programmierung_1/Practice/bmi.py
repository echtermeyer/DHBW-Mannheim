# Funktion zur Auslagerung
def bmi_calculator():
    # Das hier wäre hilfreich:
    # g = ("1" == input(Gib 1 für weiblich und 2 für männlich ein: "))
    geschlecht = input("Bitte geben Sie ihr Geschlecht ein, für weiblich X und für männlich Y: ").upper()

    # Geschlecht muss hier drinne stehen, damit es geht (theoretisch geht auch XY)
    if geschlecht not in "XY":
        raise ValueError

    weight = float(input("Dein Gewicht (in kg): ").strip().replace(",", "."))
    height = float(input("Deine Größe (in cm): ").strip().replace(",", "."))

    bmi = weight / ((height / 100) ** 2)

    if geschlecht == "X":
        if bmi < 19:
            scala = "Untergewicht"
        elif bmi <= 24:
            scala = "Normalgewicht"
        else:
            scala = "Übergewicht"
    else:
        if bmi < 20:
            scala = "Untergewicht"
        elif bmi <= 25:
            scala = "Normalgewicht"
        else:
            scala = "Übergewicht"

    print(
        "Bei einem Gewicht von {:.2f} auf eine Körpergröße von {:.2f} haben Sie einen BMI Index von: {:.2f} -> {}".format(
            weight,
            height,
            bmi,
            scala
        ))

# Try-Except um Fehler abzufangen
try:
    bmi_calculator()
except:
    print("Du hast eine falsche Eingabe getätigt!")

