# Abstand using Math
import math

p1 = (1, 2)
p2 = (4, 5)

dist = math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2))

print(dist)


# (2) Abstand using Numpy
import numpy as np

point1 = np.array((1, 2))
point2 = np.array((4, 5))

dist = np.linalg.norm(point1 - point2)

print(dist)
