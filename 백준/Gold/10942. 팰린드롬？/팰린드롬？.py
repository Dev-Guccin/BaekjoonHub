"""
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7
"""
import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int, input().split()))
M = int(input())
# 팰린드롬 dp 만들기
dp = [[0 for i in range(N)] for i in range(N)]

for i in range(N):
    s, e = 0, i
    for j in range(N-i):
        if s == e:  # 인덱스가 같으면
            dp[s][e] = 1
        elif L[s] == L[e]:  # dp[s] == dp[e]
            if s+1 == e:  # 서로 같은 글자면
                dp[s][e] = 1
            elif dp[s+1][e-1] == 1:
                dp[s][e] = 1
        s += 1
        e += 1
for m in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])
