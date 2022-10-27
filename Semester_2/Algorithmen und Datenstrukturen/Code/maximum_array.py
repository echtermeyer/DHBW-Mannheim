import random

array = random.sample(range(10, 30), 15)
highest = array[0]

for element in array[1:]:
    if element > highest:
        highest = element

print(highest)
