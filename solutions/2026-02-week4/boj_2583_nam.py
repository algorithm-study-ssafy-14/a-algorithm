import sys
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(K)]
G = [[0] * N for _ in range(M)]

for x1, y1, x2, y2 in arr:
    for y in range(y1, y2):
        for x in range(x1, x2):
            G[y][x] = 1
            
visited = [[0] * N for _ in range(M)]

dc = [0, 1, 0, -1]
dr = [1, 0, -1, 0]

ans = []

def dfs(r, c):
    visited[r][c] = 1
    area = 1
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if 0 <= nr < M and 0 <= nc < N:
            if G[nr][nc] ==0 and not visited[nr][nc]:
                area += dfs(nr, nc)
    return area

ans = []
for r in range(M):
    for c in range(N):
        if G[r][c] == 0 and not visited[r][c]:
            ans.append(dfs(r, c))

ans.sort()
print(len(ans))
print(*ans)
