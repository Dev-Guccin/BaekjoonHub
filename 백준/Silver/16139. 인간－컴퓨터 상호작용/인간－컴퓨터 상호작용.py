"""
a~z 의 문자열 dp로 저장
"""
import sys
input = sys.stdin.readline

S = input()[:-1]
Q = int(input())

dp = [[0 for i in range(len(S)+1)] for i in range(ord('a'), ord('z')+1)]

for j in range(1, len(S)+1):
    ch = S[j-1]
    for i in range(0, ord('z')-ord('a')+1):
        if chr(i+ord('a')) == ch:
            dp[i][j] = dp[i][j-1] + 1
        else:
            dp[i][j] = dp[i][j-1]

for q in range(Q):
    a, l, r = input().split()
    a = ord(a) - ord('a')
    l = int(l)+1
    r = int(r)+1
    sys.stdout.write(str(dp[a][r] - dp[a][l-1]) + '\n')
