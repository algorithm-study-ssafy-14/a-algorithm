n,m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

def get_distance(house, chicken):
    distance = 0
    for h in house:
        min_distance = float('inf')
        for c in chicken:
            min_distance = min(min_distance, abs(h[0]-c[0]) + abs(h[1]-c[1]))
        distance += min_distance
    return distance

from itertools import combinations

min_distance = float('inf')
for chicken_comb in combinations(chicken, m):
    min_distance = min(min_distance, get_distance(house, chicken_comb))
print(min_distance)