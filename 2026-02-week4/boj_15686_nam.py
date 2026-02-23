import sys
sys.stdin = open('boj_15686_nam.txt', 'r')
sys.stdin.readline

T = int(input())
for tc in range(1, 2):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    home = []
    chicken = []

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                home.append((r, c))
            elif arr[r][c] == 2:
                chicken.append((r, c))

    K = len(chicken)
    min_city_dist = float('inf')

    def dfs(start, picked):
        global min_city_dist

        if len(picked) == M:
            total = 0

            for hr, hc in home:
                min_dist = float('inf')
                for idx in picked:
                    cr, cc = chicken[idx]
                    dist = abs(hr-cr) + abs(hc-cc)
                    min_dist = min(min_dist, dist)
                total += min_dist
            
            min_city_dist = min(min_city_dist, total)
            return
        
        for i in range(start, K):
            picked.append(i)
            dfs(i + 1, picked)
            picked.pop()

    dfs(0, [])
    
    print(min_city_dist)
