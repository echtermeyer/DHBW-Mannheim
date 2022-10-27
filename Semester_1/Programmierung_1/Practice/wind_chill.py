import math

A = 13.12
B = 0.6215
C = -11.37
D = 0.3965

T = float(input("Bitte gebe die Temperatur in °C an: "))
v = float(input("Bitte gebe die Windgeschwindigkeit in km/h an: "))

WCT = A + B * T + C * pow(v, 0.16) + D * T * pow(v, 0.16)

print("Die gefühlte Temperatur beträgt: {:.2f}°C".format(WCT))