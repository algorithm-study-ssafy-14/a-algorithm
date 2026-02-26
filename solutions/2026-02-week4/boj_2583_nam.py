M, N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(K)]
G = [[0] * (N + 1) for _ in range(M + 1)]

# for row in arr:
#     print(*row)

for x1, y1, x2, y2 in arr:
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            G[y][x] = 1
            

for row in G[::-1]:
    print(*row)
