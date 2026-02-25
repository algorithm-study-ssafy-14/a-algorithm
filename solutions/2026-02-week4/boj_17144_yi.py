from copy import deepcopy

r, c, t = map(int, input().split())
first_room = [list(map(int, input().split())) for _ in range(r)]

move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

def find_visited(room):
    visited = [[False]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                visited[i][j] = True
    return visited

def munji(room, visited):
    ## 1초마다 동서남북으로 확산되고 가운데는 줄어듦
    new_room = deepcopy(room)
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0 and visited[i][j]:
                cnt = 0
                for k in range(4):
                    nx, ny = i + move_x[k], j + move_y[k]
                    if 0<=nx<r and 0<=ny<c and room[nx][ny] != -1:
                        new_room[nx][ny] += room[i][j] // 5
                        cnt += 1
                new_room[i][j] = new_room[i][j] - ((room[i][j] // 5) * cnt)
    return new_room

air_up = -1
air_down = -1
for i in range(r):
    if first_room[i][0] == -1:
        air_up = i
        air_down = i + 1
        break

def air(room):
    for i in range(air_up - 1, 0, -1):
        room[i][0] = room[i-1][0]
   
    for i in range(c - 1):
        room[0][i] = room[0][i+1]
   
    for i in range(air_up):
        room[i][c-1] = room[i+1][c-1]
 
    for i in range(c - 1, 1, -1):
        room[air_up][i] = room[air_up][i-1]
    room[air_up][1] = 0 

    for i in range(air_down + 1, r - 1):
        room[i][0] = room[i+1][0]
 
    for i in range(c - 1):
        room[r-1][i] = room[r-1][i+1]

    for i in range(r - 1, air_down, -1):
        room[i][c-1] = room[i-1][c-1]

    for i in range(c - 1, 1, -1):
        room[air_down][i] = room[air_down][i-1]
    room[air_down][1] = 0 

for i in range(t):
    if i == 0:
        one_second_later_room = munji(first_room, find_visited(first_room))
        air(one_second_later_room)
    else:
        one_second_later_room = munji(one_second_later_room, find_visited(one_second_later_room))
        air(one_second_later_room)

res = 0
for i in range(r):
    for j in range(c):
        if one_second_later_room[i][j] > 0:
            res += one_second_later_room[i][j]
print(res)
