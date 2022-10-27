# Fakultät der Zahlen von 0 bis n berechnen
def fak(n):
    if n == 0:
        return 1
    else:
        return n * fak(n-1)

#print(fak(10))

# Summe der Zahlen von 0 bis n berechnen
# (bei Zahlen kleiner 0 würde es einen Error geben)
def summe(n):
    if n == 0:
        return 0

    return n + summe(n-1)

#print(summe(0))

# String Ausrufezeichen ans Ende machen
def excl_to_end(s):
    if len(s) == 0:
        return ""

    head = s[0]
    tail = s[1:]

    tail2 = excl_to_end(tail)

    if head != "!":
        return head + tail2

    return tail2 + head

#print(excl_to_end("!!!aba!c"))

# Türme von Hanoi
def hanoi(num_plates: int, s_from: str, s_to: str, s_b: str) -> None:
    if num_plates > 0:
        hanoi(num_plates-1, s_from, s_b, s_to)
        print(f"{s_from} -> {s_to}")
        hanoi(num_plates-1, s_b, s_to, s_from)

#hanoi(2, "links", "rechts", "mitte")

def f1(n):
    if n == 0:
        return n
    return f1(n - 1) + 1

#print(f1(10))

def f2(n):
    ergebnis = 0
    while n != 0:
        ergebnis += 1
        n = n - 1

    ergebnis += n
    print(ergebnis)

#f2(10)

# f(n) =
# 1     falls n = 0
# 2*f(n//2) andernfalls

def f_1(n):
    if n == 0:
        return 1
    return 2 * f_1(n // 2)

def f_2(n):
    ergebnis = 1
    while n != 0:
        n = n // 2
        ergebnis *= 2

    return ergebnis * 1 # Basisfall

print(f_1(123124))
print(f_2(123124))
