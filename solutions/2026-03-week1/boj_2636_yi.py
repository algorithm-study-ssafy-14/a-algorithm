from collections import deque
from copy import deepcopy

y, x = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(y)]

move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

def bfs():
    visited = [[False]*x for _ in range(y)]
    queue = deque([(0,0)])
    visited[0][0] = True

    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx, ny = vx + move_x[i], vy + move_y[i]
            if 0<=nx<y and 0<=ny<x and not visited[nx][ny]:
                if cheese[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    return visited

def cheese_cnt():
    total_cheese = 0
    for i in range(y):
        for j in range(x):
            if cheese[i][j] == 1:
                total_cheese += 1
    return total_cheese

time = 0
last_cheese = 0

while True:
    new_cheese = bfs()
    total_cheese = cheese_cnt()

    if total_cheese == 0:
        break
    last_cheese = total_cheese
    melt_cheese = []
    for i in range(y):
        for j in range(x):
            if cheese[i][j] == 1:
                for k in range(4):
                    nx, ny = i + move_x[k], j + move_y[k]
                    if 0<=nx<y and 0<=ny<x and new_cheese[nx][ny]:
                        melt_cheese.append((i,j))
                        break
    for r,c in melt_cheese:
        cheese[r][c] = 0
    time += 1

print(time)
print(last_cheese)
