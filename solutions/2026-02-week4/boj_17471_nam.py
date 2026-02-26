import sys
sys.stdin = open('boj_17471_nam.txt', 'r')
input = sys.stdin.readline
from itertools import combinations

T = int(input())

for tc in range(1, T + 1):
    N = int(input())                         
    popularation = list(map(int, input().split()))           

    G = [[] for _ in range(N + 1)]

    for i in range(1, N + 1):
        arr = list(map(int, input().split()))     
        k = arr[0]

        if k:
            G[i] = arr[1:]

    # print(G)

    A = []
    B = []

    result = -1

    # 적어도 하나의 구역 포함
    # 연결되어 있지 않은 경우
    # 인구 차이 최솟값
    min_pop = int('inf')

    def bfs(start, cnt):
        global min_pop

        if len(A) == 0 or len(B) == 0:
            return
        
        if cnt == N:
            pass
            return
        
        for i in range(start, N):
            A.append(i)
            bfs(i + 1, cnt)
            A.pop()

    bfs(1, 0)

        


