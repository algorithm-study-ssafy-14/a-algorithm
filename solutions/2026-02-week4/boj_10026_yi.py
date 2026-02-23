# from collections import deque

# n = int(input())
# color = [input() for _ in range(n)]

# def bfs(graph, start_x, start_y):
#     visited = [[False]*n for _ in range(n)]
#     queue = deque([start_x, start_y])
#     visited[start_x][start_y] = True

#     while queue:
#         vx, vy = queue.popleft()
#         for i in graph[vx][vy]:
#             if i == color[vx][vy] and not visited[]:
                
