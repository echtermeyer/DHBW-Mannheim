l1 = [1, 2, 3, "hallo"]

t1 = tuple(l1)

l2 = list(t1)
l2.append(4)

t1 = tuple(l2)

print(t1)