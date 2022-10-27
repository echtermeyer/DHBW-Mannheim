import random

regen = (1 == random.randrange(2))
temperatur = random.randrange(30)

print(temperatur, regen)

print("Hubert geht mit Betty Gassi\n")

if regen:
    print("Regenschirm")
elif not regen and temperatur > 15:
    print("Bier und Buch")

if regen or 22 <= temperatur <= 24:
    print("Baum")
else:
    print("Wiese")

if regen and temperatur > 10:
    for i in range(10):
        print("Wuff")
elif temperatur < 5:
    for i in range(3):
        print("Wuff")
elif not regen and temperatur > 20:
    for i in range(30):
        print("Wuff")
else:
    print("Wuff")
