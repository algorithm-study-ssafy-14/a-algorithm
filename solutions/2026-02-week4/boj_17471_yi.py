from collections import deque
from itertools import combinations

n = int(input())
population = list(map(int, input().split()))
visited = [False] * n
graph = [[] for _ in range(n)]
for i in range(n):
    cities = list(map(int, input().split()))
    for j in range(cities[0]):
        graph[i].append(cities[j + 1] - 1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    cnt = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt

res = float('inf')

for i in range(1, n//2+1):
    for group_a in combinations(range(n), i):
        group_a = list(group_a) 
        group_b = []
        for x in range(n):
            if x not in group_a:
                group_b.append(x)

        visited_a = [True] * n
        for i in group_a:
            visited_a[i] = False
        
        res_a = bfs(graph, group_a[0], visited_a)

        visited_b = [True] * n
        for j in group_b:
            visited_b[j] = False
            
        res_b = bfs(graph, group_b[0], visited_b)

        if res_a == len(group_a) and res_b == len(group_b):
            sum_a = sum(population[idx] for idx in group_a)
            sum_b = sum(population[idx] for idx in group_b)
            res = min(res, abs(sum_a - sum_b))

if res == float('inf'):
    print(-1)
else:
    print(res)
