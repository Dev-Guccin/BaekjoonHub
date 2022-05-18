"""
역속적인 날짜의 합을 구하기 때문에 누적합
"""

N, K = map(int, input().split())
T = list(map(int, input().split()))

f = 0
# 초기값
for i in range(K):
    f += T[i]
L = 0
R = K-1
answer = f
while True:

    R += 1
    if R == N:
        break
    f += T[R]
    f -= T[L]
    L += 1

    answer = max(answer, f)
print(answer)
