from collections import deque

T = int(input())
for test_case in range(T):
    m, n, k = map(int, input().split())
    garden = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        garden[y][x] = 1
    
    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]

    def bfs(graph, i, j):
        queue = deque([(j,i)])
        visited[i][j] = True

        while queue:
            vx, vy = queue.popleft()
            for k in range(4):
                nx, ny = vx + move_x[k], vy + move_y[k]
                if 0<=nx<m and 0<=ny<n and graph[ny][nx] == 1:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if garden[i][j] == 1 and not visited[i][j]:
                bfs(garden, i, j)
                cnt += 1
    
    print(cnt)