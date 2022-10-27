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
seperator(9)

female = False  # ("1" == input("Bist du weiblich? 1 für Bestätigung: ").strip())
weight = 90  # float(input("Gewicht in kg: ").strip().replace(",", "."))
height = 2.02  # float(input("Größe in m: ").strip().replace(",", "."))

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


# 9.) hairdresser
seperator(9)

female = True  # ("1" == input("Für weiblich 1, sonst 0: ").strip())
age = 67  # int(input("Dein Alter: ").strip())
dyeing = 0  # ("1" == input("Dyeing hair?: ").strip())
drying = 1  # ("1" == input("Drying hair?: ").strip())

total = 0

if female and age <= 16:
    total += 12
elif female:
    total += 20
elif not female and age <= 14:
    total += 10
else:
    total += 15

if dyeing: total += 10
if drying: total += 5

print(total)


# 10.) random numbers
seperator(10)

from random import random

trys = 0

while True:
    trys += 1
    x = random()

    if x > 0.999:
        break

print(trys, x)


# 11.) reverse string order
seperator(11)

s = "Hallo"
print(s[::-1])

s2 = ""
for i in range(len(s)-1, -1, -1):
    s2 += s[i]
print(s2)

s3 = ""
for c in s:
    s3 = c + s3
print(s3)


# 12.) div7 & mult5 & 2000-3200
seperator(12)

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=" ")
print()


# 13.) caesar-chiffre
seperator(13)

text = "helloworld"
chiffre = ""
key = 4

for c in text:
    chiffre += chr(ord(c) + key)
print(chiffre)


# 14.) greatest common divisor
seperator(14)

a = 72
b = 52

while b != 0:
    h = a % b
    a = b
    b = h

print(a)


# 15.) fibonacci
seperator(15)

a, b = 0, 1

while a < 10:
    print(a, end=" ")
    a, b = b, a+b
print()


# 16.) lists
seperator(16)

import random

a = [random.random() for _ in range(100)]
a.sort(reverse=True)
print(a)


# 17.) dicts
seperator(17)

us_constitution = "Ich schöwre, dass ich hier meinen Eid schöre, in meinen Adern fließt Blut"
us_constitution_list = us_constitution.split(" ")

counter = dict()

for word in us_constitution_list:
    if word in counter.keys():
        counter[word] += 1
    else:
        counter[word] = 1

print(counter)


# 18.) 100 random positives
seperator(18)
from random import randrange

positives = [temp for _ in range(100) if (temp := randrange(-100, 100)) < 0]
print(positives)


# 19.) abs
seperator(19)
walrus_op = [abs(temp) for _ in range(100) if (temp := randrange(-100, 100)) < 0]
abs_list = [abs(i) for i in positives]

print(walrus_op)
print(abs_list)


# 20.) banana list comp
seperator(20)

freshfruit = [" banana", " loganberry ", "passion fruit "]
freshfruit_stripped = [i.strip() for i in freshfruit]

print(freshfruit_stripped)

a = positives.copy()
a_squared = [pow(i, 2) for i in a]

print(a_squared)


# 21.) for umschreiben to comp
seperator(21)

sentence = "the quick brown fox jumps over the lazy dog"
word_lengths = [len(word) for word in sentence.split() if word != "the"]

print(word_lengths)


# 22.) list comp zahlen
seperator(22)

numbers = [i for i in range(1, 1001) if i % 7 == 0]

print(numbers)


# 23.) 1-1000 with 3 as digit
seperator(23)

numbers = [i for i in range(1, 1001) if "3" in str(i)]

print(numbers)


# 24.) string to non vowel
seperator(24)

teststring = "Find all of the words in a string that are less than 4 letters"
vowels = "aeiou "

non_vowels = "".join([i for i in teststring if i.lower() not in vowels])

print(non_vowels)


# 25.) dict comp
seperator(25)

sentence = teststring
lengths = {word:len(word) for word in sentence.split()}

print(lengths)


# 26.) multi funct
seperator(26)

from typing import List

def temperatur(temps: List[float]):
    print(min(temps), max(temps), sum(temps)/len(temps), sorted(temps)[len(temps)//2])

temperatur([1, 2, 4, 1, 4, 2.5])


# 27.) christmas tree
seperator(27)

def christmas_tree(height=4):
    if height < 4:
        return

    tree = ""
    for i in range(height-2, 0, -1):
        tree = " "*(height-i) + "*"*(i*2-1) + " "*(height-i) + "\n" + tree

    tree = tree + 2*((height-1)*" " + "*" + (height-1)*" " + "\n")

    return tree

print(christmas_tree(20))


# 28.) quersumme
seperator(28)

def quersumme(digit):
    if digit == 0:
        return 0

    return digit % 10 + quersumme(digit // 10)

print(quersumme(12331))


# 29.) fib number
seperator(29)

def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)

print(fib(4))


# 30) rekursive and iterative
seperator(30)

def g1(u, v):
    if u == 0:
        return v
    elif u % 2 == 0 and v % 2 == 0:
        return 2 * g1(u//2, v//2)
    elif u % 2 == 0:
        return g1(u//2, v)
    else:
        return g1(abs(u-v), min(u, v))

def g2(u, v):
    ergebnis = 1
    while u != 0:
        if u % 2 == 0 and v % 2 == 0:
            ergebnis *= 2
            u //= 2
            v //= 2
        elif u % 2 == 0:
            u //= 2
        else:
            u, v = abs(u-v), min(u, v)

    ergebnis *= v
    return ergebnis

print(g1(10, 3))
print(g2(10, 3))


# 31.) person
seperator(31)

from datetime import datetime, timedelta

class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def person_age(self):
        return timedelta