import sys
# sys.stdin = open('boj_2644_nam.txt', 'r')
input = sys.stdin.readline
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
G = [[] for _ in range(n + 1)] 
for i in range(m):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)


def bfs(G, v, n):   # G: 그래프 v: 현재 노드 n: 노드 수
    visited = [0] * (n + 1)
    Q = deque()
    Q.append(v)
    visited[v] = 1
    D = [0] * (n + 1)   # 최단 경로
    P = [0] * (n + 1)   # 최단 경로 루트

    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = 1
                D[w] = D[v] + 1
                P[w] = v
    
    return D[b] if visited[b] else -1
    
ans = bfs(G, a, n)
print(ans)