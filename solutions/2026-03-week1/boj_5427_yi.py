from collections import deque

def solve():
    w, h = map(int, input().split())
    building_map = [list(input()) for _ in range(h)]
    
    user_q = deque()
    fire_q = deque()
    dist = [[-1] * w for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if building_map[i][j] == '@':
                user_q.append((i, j))
                dist[i][j] = 0
            elif building_map[i][j] == '*':
                fire_q.append((i, j))

    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]

    time = 0
    while user_q:
        time += 1
        for _ in range(len(fire_q)):
            fx, fy = fire_q.popleft()
            for i in range(4):
                nfx, nfy = fx + move_x[i], fy + move_y[i]
                if 0 <= nfx < h and 0 <= nfy < w and building_map[nfx][nfy] in ('.', '@'):
                    building_map[nfx][nfy] = '*'
                    fire_q.append((nfx, nfy))
        
        for _ in range(len(user_q)):
            ux, uy = user_q.popleft()
            for i in range(4):
                nx, ny = ux + move_x[i], uy + move_y[i]
                
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    return time
                
                if building_map[nx][ny] == '.' and dist[nx][ny] == -1:
                    dist[nx][ny] = time
                    user_q.append((nx, ny))
                    
    return "IMPOSSIBLE"

t = int(input())
for _ in range(t):
    print(solve())