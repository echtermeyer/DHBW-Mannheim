# Part One
def get_last_two():
    x = input("Gib eine Zahl ein: ")

    d_1 = x[-1]
    d_2 = x[-2]

    print("Last Digit: " + d_1)
    print("Second Last Digit: " + d_2)

get_last_two()

# Part Two:
def get_last_two_2():
    x = int(input("Gib eine Zahl ein: "))

    d_1 = x % 10

    rest = x // 10
    d_2 = rest % 10

    print("Last Digit: ", d_1)
    print("Second Last Digit: ", d_2)

get_last_two_2()