def approx_pi(n: int) -> float:
    if n == 0:
        return 4

    # Wiederspiegelung der Funktion aus der Aufgabenstellung
    return approx_pi(n - 1) + 4 * (pow(-1, n) / (2*n + 1))

print(approx_pi(100))


def a2(n):
    ergebnis = 0
    while n > 0:
        ergebnis = ergebnis + 4 * (pow(-1, n) / (2*n + 1))
        n -= 1
    ergebnis += 4
    return ergebnis

print(a2(100))
