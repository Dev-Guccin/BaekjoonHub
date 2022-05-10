"""
5 3
1 2 3 1 2
"""

N, M = map(int, input().split())
data = list(map(int, input().split()))

tmp = 0
count = 0
mdp = [0 for i in range(M)]
for i in range(N):
    tmp += data[i]

    if tmp % M == 0:
        count += 1
    mdp[tmp % M] += 1
for i in range(M):
    count += int(mdp[i] * (mdp[i]-1) / 2)
print(count)
