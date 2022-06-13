"""
투포인터로 구하기
"""

N, S = map(int, input().split())
M = list(map(int, input().split()))

L = 0
R = 0
INF = 100000
answer = INF
total = M[L]
while R < len(M):
    # 합이 성립하는지 판별
    if total < S:  # 만족하지 않으므로 R을 더한다.
        R += 1
        if R >= len(M):
            break
        total += M[R]
    else:  # 만족하므로 수를 갱신하고 L을 더한다.
        answer = min(answer, R-L + 1)
        total -= M[L]
        L += 1

if INF == answer:
    print(0)
else:
    print(answer)
