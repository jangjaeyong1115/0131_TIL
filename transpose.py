matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2],
]

transposed_matrix = [[0] * 3 for _ in range(4)]

for i in range(4):
    for j in range(3):
        transposed_matrix[i][j] = matrix[j][i]

    print(transposed_matrix)