from collections import deque

## 4 0 6 2
## 1 1 2 5
## 0 2 4 4
def cal_rec(x, y, a, b):
    for i in range(abs(b - m), abs(y - m)):
        for j in range(x, a):
            paper[i][j] = 1

move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

def bfs(graph, s_x, s_y):
    queue = deque([(s_x, s_y)])
    visited[s_x][s_y] = 1
    res = 1

    while queue:
        vx, vy = queue.popleft()
        for i in range(4):
            nx, ny = vx + move_x[i], vy + move_y[i]
            if 0<=nx<m and 0<=ny<n:
                # print(nx, ny)
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    res += 1
                    queue.append((nx,ny))
    
    return res

m,n,k = map(int, input().split())
paper = [[0]*n for _ in range(m)]
visited = [[0]*n for _ in range(m)]

for i in range(k):
    x, y, a, b = map(int, input().split())
    cal_rec(x,y,a,b)

# for i in range(m):
#     print(paper[i], sep="\n")

res = 0
cnt = 0
res_list = []
for i in range(m):
    for j in range(n):
        if paper[i][j] == 0 and visited[i][j] == 0:
            res = bfs(paper, i, j)
            cnt += 1
            res_list.append(res)

res_list.sort()
print(cnt)
print(*res_list)