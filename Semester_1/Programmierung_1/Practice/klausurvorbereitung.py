def seperator(number):
    print("\n" + "#"*10 + f" Exercise {number} " + "#"*10)

# 1.) last and second last digits of a number
seperator(1)
number = 1241

last = number % 10
second_last = number // 10 % 10

print(last, second_last)


# 2.) calculate area of a circle
seperator(2)
import math

r = 4
area = math.pi * pow(4, 2)
print(area)


# 3.) euclidian distance
seperator(3)
import math

xy1 = (2, 3)
xy2 = (5, 6)

distance = math.sqrt((xy1[0] - xy2[0])**2 + (xy1[1] - xy2[1])**2)
print(distance)


# 4.) string output
seperator(3)
s = """Sample string:
a string that you "don't" have to escape
This
is a ....... mulit-line
string --------> example"""
print(s)


# 5.) x y swap
seperator(5)

x = 5
y = 3

x, y = y, x
print(x, y)


# 6.) print end= modified
seperator(6)

print("Hallo", end=" ")
print("World")


# 7.) wind-chill
seperator(7)

A = 13.12
B = 0.6215
C = -11.37
D = 0.3965

t = 0  # float(input("Temperatur in °C: ").strip().replace(",", "."))
v = 0  # float(input("Windgeschwindigkeit in km/h: ").strip().replace(",", "."))

wct = A + B*t + C*v**0.16 + D*t*v**0.16
print(wct)


# 8.) betty
seperator(8)

import random

regen = (1 == random.randrange(2))
temperatur = random.randrange(30)

if regen:
    print("Regenschirm")
elif temperatur > 15:
    print("Bier und Buch")

if regen or 22 <= temperatur <= 24:
    print("Baum")
else:
    print("Wiese")

if temperatur > 10 and regen:
    print(10)
elif temperatur < 5:
    print(3)
elif temperatur > 20 and not regen:
    print(30)
else:
    print(1)


# 9.) bmi
female = ("1" == input("Bist du weiblich? 1 für Bestätigung").strip())
weight = float(input("Gewicht in kg: ").strip().replace(",", "."))
height = float(input("Größe in m: ").strip().replace(",", "."))

bmi = (weight / (height ** 2))

type = "Normalgewicht"
if female:
    if bmi < 19:
        type = "Untergewicht"
    if bmi > 24:
        type = "Übergewicht"
else:
    if bmi < 20:
        type = "Untergewicht"
    if bmi > 25:
        type = "Übergewicht"

print("Bei einem Gewicht von {} auf eine Körpergröße von {}m haben Sie einen BMI Index von: {:.2f} -> {}".format(
    weight, height, bmi, type
))
