from collections import deque

n, m = map(int, input().split())
map_ = [list(input()) for _ in range(n)]

move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

def bfs(graph, start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = 0
    res = 0

    while queue:
        vx, vy = queue.popleft()

        for i in range(4):
            nx, ny = vx + move_x[i], vy + move_y[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'L':
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[vx][vy] + 1
                    res = max(res, visited[nx][ny])
                    queue.append([nx, ny])
    return res

max_res = -1
for i in range(n):
    for j in range(m):
        if map_[i][j] == 'L':
            visited = [[-1]*m for _ in range(n)]
            max_res = max(max_res, bfs(map_, i, j))
            
print(max_res)
