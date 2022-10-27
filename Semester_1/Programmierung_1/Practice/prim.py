def get_prims(a, b):
    prims = []

    for i in range(a, b+1):
        not_prim = False
        for j in range(2, i):
            if i % j == 0:
                not_prim = True
                break

        if not not_prim and i > 1:
            prims.append(i)

    return prims

print(get_prims(10, 20))