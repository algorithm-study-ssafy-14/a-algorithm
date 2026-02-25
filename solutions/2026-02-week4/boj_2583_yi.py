# from collections import deque

# m,n,k = map(int, input().split())
# paper = [[0]*n for _ in range(m)]
# visited = [[0]*n for _ in range(m)]
# for i in range(k):
#     x, y, a, b = map(int, input().split())

# move_x = [-1, 1, 0, 0]
# move_y = [0, 0, -1, 1]

# def bfs(graph, s_x, s_y, e_x, e_y):
#     queue = deque([(s_x, s_y)])
#     visited[s_x][s_y] = 1

#     while queue:
#         vx, vy = queue.popleft()
#         for i in range(4):
#             nx, ny = vx + move_x[i], vy + move_y[i]
#             if 0<=nx<n and 0<=ny<m:
#                 if visited[nx][ny] == 0:
#                     visited[nx][ny] = 1
#                     queue.append((nx,ny))