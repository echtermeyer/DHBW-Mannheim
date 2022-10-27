n = 0

def fak(n):
    res = 1
    for i in range(1, n+1):
        res *= i

    return res

print(fak(n))
