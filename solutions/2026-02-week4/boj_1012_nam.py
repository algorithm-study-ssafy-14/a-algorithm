# import sys
# sys.stdin = open('boj_1012_nam.txt', 'r')
# input = sys.stdin.readline

import sys
sys.setrecursionlimit(10**6)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c):
    visited[r][c] = True
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if 0 <= nr < N and 0 <= nc < M:
            if G[nr][nc] and not visited[nr][nc]:
                dfs(nr, nc)

T = int(input())
for tc in range(1, T + 1):
    M, N, K = map(int, input().split())

    G = [[False] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        c, r = map(int, input().split())
        G[r][c] = True

    cnt = 0    
    for i in range(N):
        for j in range(M):
            if G[i][j] and not visited[i][j]:
                dfs(i, j)
                cnt += 1
    
    print(cnt)


        


