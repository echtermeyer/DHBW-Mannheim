# Aufgabe 1:
print("\nAufgabe 1:")
# Loop, die bis 0-10 zählt und diese ausgibt
for i in range(11):
    print(i, end=" ")
print()

# Loop, die 0-20 in 5er Schritten zählt
for i in range(0, 21, 5):
    print(i, end=" ")
print()

# Loop von 4-34 in 5er Schritten
for i in range(4, 35, 5):
    print(i, end=" ")
print()

# Loop von 11-1 in 2er Schritten
for i in range(11, 0, -2):
    print(i, end=" ")
print("\n")


# Aufgabe 2:
print("\nAufgabe 2:")
# While Loop 0-7
i = 0
while i <= 7:
    print(i, end=" ")
    i += 1
print("\n")

# While Loop, 3er Schritte, a enthält Summe aus Iteration (kein print in Aufgabenstellung)
a = 0
i = 2
while i < 20:
    a += i
    # Print nicht in Aufgabe gefordert, aber sinnvoll für Kontrolle
    print(i, a)
    i += 3
print()


# Aufgabe 3:
print("\nAufgabe 3:")
# While Loop 0-7
i = 0
while True:
    if i > 7:
        break
    print(i, end=" ")
    i += 1
print("\n")

# Loop von 2 bis 20 in 3er als while mit break
a = 0
i = 2
while True:
    if i > 19:
        break
    a += i
    # Print nicht in Aufgabe gefordert, aber sinnvoll für Kontrolle
    print(i, a)
    i += 3
print()


# Aufgabe 4
print("\nAufgabe 4:")
# Anlegen der Variablen
a, b = 20, 3

# Schleifen als Funktion, um eine bessere Übersicht zu haben
def calc_div(dividend, divisor):
    # Counter ist das Result, wie oft passt der divisor in den dividend
    counter = 0
    remainder = dividend

    # Wenn der divisor in den remainder reinpasst, dann wird der counter erhöht und der divisor vom remainder abgezogen
    while remainder >= divisor:
        counter += 1
        remainder -= divisor

    return counter

# Mit den vorgegebenen Werten testen
# print(calc_div(a, b)) (ist nur zum testen da, daher auskommentiert)
print()

# Mit For-Loops
for i in range(30, 0, -1):
    for j in range(2, 5, 1):
        print(f"{i} // {j} = ", end=" ")
        print(calc_div(i, j))
