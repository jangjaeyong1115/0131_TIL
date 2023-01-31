matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2],
]

print(matrix)

# 1. 행 우선 순회

N = len(matrix)
M = len(matrix[0])
for i in range(3):
    for j in range(4):
        print(matrix[i][j], end=" ")

print()

# 2. 열 우선 순회

for i in range(4):
    for j in range(3):
        print(matrix[j][i],end=" ")
    print()


# 3. 총합

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2],
]

N = len(matrix)
M = len(matrix[0])

cnt = 0
for i in range(N):
    for j in range(M):
        cnt += matrix[i][j]

    print(cnt)