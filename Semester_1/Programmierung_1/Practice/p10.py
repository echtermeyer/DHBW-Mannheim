# Quersumme einer Zahl berechnen
def quersumme(s):
    if len(s) == 0:
        return 0

    head = s[0]
    tail = s[1:]

    return int(head) + quersumme(tail)

print(quersumme("235532"))


def quersumme_digit(d):
    if d // 10 == 0:
        return d % 10

    return quersumme_digit(d // 10) + d % 10

print(quersumme_digit(235))


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

print(fib(3))

