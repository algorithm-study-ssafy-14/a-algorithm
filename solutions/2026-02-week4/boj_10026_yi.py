from collections import deque

n = int(input())
color = [list(input()) for _ in range(n)]  ## 문자열 수정 불가능하니까 리스트로 받아야됨
visited = [[False]*n for _ in range(n)]

move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

def bfs(graph, start_x, start_y):
    queue = deque([(start_x, start_y)]) ## 인자로 들어온 데이터 순회하면서 꺼내야하기 대문에 묶어줘야됨
    visited[start_x][start_y] = True

    while queue:
        vlist = queue.popleft()
        vx, vy = vlist
        for i in range(4):
            nx, ny = vx + move_x[i], vy + move_y[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == color[start_x][start_y]:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

cnt = 0      
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(color, i, j)
            cnt += 1
print(cnt, end=' ')

for i in range(n):
    for j in range(n):
        if color[i][j] == 'G':
            color[i][j] = 'R'

visited = [[False]*n for _ in range(n)]
cnt = 0      
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(color, i, j)
            cnt += 1
print(cnt)