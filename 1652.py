import sys

N = int(sys.stdin.readline().rstrip())
positions, rotate_positions = [['']*N for _ in range(N)], [['']*N for _ in range(N)]
posible, rotate_posible = 0, 0

for _ in range(N):
    position = sys.stdin.readline().rstrip()
    
    for i in range(len(position)):
        positions[_][i] = position[i]

for n in range(N):
    for m in range(N):
        rotate_positions[n][m] = positions[-m-1][n]

for position in positions:
    join_position = ''.join(position).split('X')
    for join in join_position:
        if len(join) >= 2:
            posible += 1

for position in rotate_positions:
    join_position = ''.join(position).split('X')
    for join in join_position:
        if len(join) >= 2:
            rotate_posible += 1

print(posible, rotate_posible)