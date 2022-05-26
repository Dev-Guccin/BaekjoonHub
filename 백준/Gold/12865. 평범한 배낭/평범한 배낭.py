N, K = map(int, input().split())
W = [0]
V = [0]

for i in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

dp = [[0 for i in range(K+1)] for i in range(N+1)]


def ns(n, k):
    if dp[n][k] != 0:
        return dp[n][k]
    if n <= 0 or k <= 0:  # n이 0이면 선택하는게 없는거,  k가 0보다 작으면 연산 무의미
        return 0
    exist = 0
    if k >= W[n]:
        exist = ns(n-1, k - W[n]) + V[n]
    noExist = ns(n-1, k)
    dp[n][k] = max(exist, noExist)
    return dp[n][k]


print(ns(N, K))
