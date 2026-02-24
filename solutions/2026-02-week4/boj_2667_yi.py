from collections import deque

n = int(input())
home = [list(map(int, input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

def bfs(graph, start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    h_cnt = 1

    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx, ny = vx + move_x[i], vy + move_y[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    h_cnt += 1
    return h_cnt

res_list = []
res = 0
for i in range(n):
    for j in range(n):
        if home[i][j] == 1 and not visited[i][j]:
            temp = bfs(home, i, j)
            # if temp != 1:
            res_list.append(temp)
            res += 1

print(res)
res_list.sort()
for i in range(len(res_list)):
    print(res_list[i])