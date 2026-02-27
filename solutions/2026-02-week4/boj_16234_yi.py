from collections import deque

n, l ,r = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]

move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

def bfs(graph, i, j):
    queue = deque([(i, j)])
    visited[i][j] = 1
    union_con = [(i, j)]

    while queue:
        vx, vy = queue.popleft()
        # print(f"팝한 값: {vx, vy} {graph[vx][vy]}")
        for i in range(4):
            nx, ny = vx + move_x[i], vy + move_y[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    temp = abs(graph[nx][ny] - graph[vx][vy])
                    if l <= temp <= r:
                        union_con.append((nx, ny))
                        # print(f"리스트안에 들어있는값: {union_con}")
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
    return union_con

def union_counry(union_con, temp):
    for x, y in union_con:
        countries[x][y] = temp
    return countries

open_door = 0
while True:
    visited = [[-1]*n for _ in range(n)]
    flag = False
    res_list = []
    temp = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                if open_door == 0:
                    res_list = bfs(countries, i, j)
                    if len(res_list) > 1:
                        # print(res_list)
                        temp = sum(countries[x][y] for x, y in res_list) // len(res_list)
                        new_contries = union_counry(res_list, temp)
                        flag = True
                else:
                    res_list = bfs(new_contries, i, j)
                    if len(res_list) > 1:
                        # print(f"인구이동 {open_door} : {res_list}")
                        temp = sum(countries[x][y] for x, y in res_list) // len(res_list)
                        new_contries = union_counry(res_list,temp)
                        flag = True

    if flag:
        open_door += 1
    else:
        break

print(open_door)