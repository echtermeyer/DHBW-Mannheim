"""a = ["Moin", "Guten Tag", "Tach", "Hallöchen"]
b = ["Peter", "Marie", "Lea"]

greetings = []

for i in a:
    for j in b:
        greetings.append(i + " " + j)

print(greetings)"""


a = [
    i+j
    for i in ["a", "b"]
    for j in ["1", "2"]
]
print(a)