import sys
sys.stdin = open('boj_17144_nam.txt', 'r')
input = sys.stdin.readline

T = int(input())
for i in range(1, T + 1):
    R, C, T = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(R)]
    matrix = [[-1] * C for _ in range(R)]
    matrix_cnt = [[0] * C for _ in range(R)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for r in range(R):
        for c in range(C):
            if arr[r][c] >= 5:
                matrix[r][c] = arr[r][c] // 5
    
    for r in range(R):
        for c in range(C):
            if matrix[r][c] != -1:
                for dir in range(4):
                    cnt = 0
                    nr = r + dr[dir]
                    nc = c + dc[dir]
                    if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                        arr[nr][nc] += matrix[r][c]
                        cnt += 1
                    matrix_cnt[r][c] += cnt

    for r in range(R):
        for c in range(C):
            if matrix[r][c] != -1:
                arr[r][c] -= matrix[r][c] * matrix_cnt[r][c]
    
    dust = 0
    for r in range(R):
        for c in range(C):
            if arr[r][c] == -1:
                if c == 0:
                    arr[r-1][c] = 0
                    arr[r+2][c] = 0
                else:
                    arr[r][c-1] = 0
                    arr[r][c+2] = 0
                continue
            
            dust += arr[r][c]
    
    print(dust)