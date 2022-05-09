"""
빌딩의 시야각이 접하지 않아야 보이는거
=> 기울기를 판단하여 가능한지 안한지 확인한다.

15
1 5 3 2 6 3 2 6 4 2 5 7 3 1 5
"""
N = int(input())
S = [0 for i in range(N)]
B = list(map(int, input().split()))

for i in range(N):
    maxDegree = -1000000000
    y = B[i]
    x = i
    for j in range(i+1, N):
        ty = B[j]
        tx = j

        if maxDegree < (ty-y)/(tx-x):
            maxDegree = (ty-y)/(tx-x)
            S[i] += 1
            S[j] += 1
print(max(S))
