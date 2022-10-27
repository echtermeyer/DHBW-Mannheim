matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print(transposed_matrix)

# import random
# res = [i for i in random.randrange(-100, 100) if i >= 0]