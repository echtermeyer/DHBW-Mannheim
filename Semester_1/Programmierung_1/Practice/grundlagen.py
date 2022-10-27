# Aufgabe 1:
def divide_int(a: int, b: int) -> int:
    # Sobald diese Bedingung wahr ist, passt b nicht mehr in a
    if a - b < 0:
        return 0

    # +1 dient sozusagen als Counter
    return divide_int(a-b, b) + 1

# print(divide_int(20, 3))


# Aufgabe 2:
def pow(a: int, b: int) -> int:
    # b == 0 checken, um den Sonderfall abzudecken
    if b == 0:
        return 1
    if b == 1:
        return a

    # Aneinanderreihung von a's
    return a * pow(a, b - 1)

# print(pow(1, 4))


# Aufgabe 3:
def countdown(n: int) -> None:
    if n == 0:
        print(n)
    else:
        # Erst wird n gedruckt, dann wird die Funktion wieder aufgerufen
        print(n)
        countdown(n - 1)

# countdown(20)


# Aufgabe 4:
def countup(n: int) -> None:
    if n == 0:
        print(n)
    else:
        # Die Funktion wird aufgerufen, erst dann print. Da es von hinten aufgerollt wird,
        # kommt es zum countup
        countup(n - 1)
        print(n)

# countup(20)


# Aufgabe 5:
def approx_pi(n: int) -> float:
    if n == 0:
        return 1

    # Wiederspiegelung der Funktion aus der Aufgabenstellung
    return approx_pi(n - 1) + pow(-1, n) / (2*n + 1)

# print(approx_pi(100))


# Aufgabe 6:
def f(x: int, y: int) -> int:
    erg = 0
    while x != y:
        erg += x
        x, y = (x + y) // 2, x

    erg += x

    return erg
print(f(20, 10))
# print(f(202, 3.5))


# Aufgabe 7:
def switch_case(s: str) -> str:
    if len(s) == 0:
        return ""

    head = s[0]
    tail = s[1:]

    # Unverändert, falls head kein Buchstabe ist
    if not head.isalpha():
        return head + switch_case(tail)

    # Schauen, ob head upper_case ist
    is_upper = 65 <= ord(head) <= 90

    if is_upper:
        # Um lower() zu machen, benötigt man +32 in ASCII
        modified_head = chr(ord(head) + 32)
    else:
        # Um upper() zu machen, benötigt man -32 in ASCII
        modified_head = chr(ord(head) - 32)

    return modified_head + switch_case(tail)

# print(switch_case("Programmierung 1 WiSe 2021/22"))