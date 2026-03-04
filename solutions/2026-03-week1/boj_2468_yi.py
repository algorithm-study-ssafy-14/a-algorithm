from collections import deque

n = int(input())
city = [list(map(int,input().split())) for _ in range(n)]

move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

def flood(rain):
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if city[i][j] <= rain:
                visited[i][j] = True
    return visited

def no_flood(no_safe, visited, k, h):
    queue = deque([(k,h)])
    while queue:
        vx,vy = queue.popleft()
        for i in range(4):
            nx, ny = vx + move_x[i], vy + move_y[i]
            if 0<=nx<n and 0<=ny<n and not no_safe[nx][ny]:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

max_cnt = -1
for i in range(100, -1, -1):
    visited = [[False]*n for _ in range(n)]
    # print(f"i : {i}")
    no_safe = flood(i)
    cnt = 0
    for k in range(n):
        for h in range(n):
            if not no_safe[k][h] and not visited[k][h]:
                no_flood(no_safe, visited, k, h)
                cnt += 1
    max_cnt = max(max_cnt, cnt)
    # print(f"{max_cnt} : {max_cnt}")
print(max_cnt)