import sys
sys.setrecursionlimit(10**6)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

G = [[0] * N for _ in range(N)]

mx = max(map(max, arr))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c):
    visited[r][c] = 1
    area = 1
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if 0 <= nr < N and 0 <= nc < N:
            if G[nr][nc] == 0 and not visited[nr][nc]:
                area += dfs(nr, nc)

    return area

result = 0

for i in range(0, mx):
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] <= i:
                G[r][c] = 1
            else:
                G[r][c] = 0

    ans = []
    for r in range(N):
        for c in range(N):
            if G[r][c] == 0 and not visited[r][c]:
                ans.append(dfs(r, c))
    
    i_area = len(ans)
    result = max(result, i_area)

print(result)

