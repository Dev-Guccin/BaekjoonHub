"""
그리디와 최소힙으로 구하기
"""
import heapq
import sys
input = sys.stdin.readline
N = int(input())
hq = []
cl = []
for n in range(N):
    a, b = map(int, input().split())
    cl.append([a, b])
cl.sort()

for c in cl:
    a, b = c
    if len(hq) == 0:
        heapq.heappush(hq, [b, a])
        continue

    end, start = heapq.heappop(hq)
    if end <= a:
        heapq.heappush(hq, [b, start])
    else:
        heapq.heappush(hq, [end, start])
        heapq.heappush(hq, [b, a])
print(len(hq))
