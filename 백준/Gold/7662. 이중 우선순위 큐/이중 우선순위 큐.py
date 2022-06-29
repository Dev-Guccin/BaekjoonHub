"""


7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1

D 1은 최댓값 삭제
D -1은 최솟값을 삭제 => 그냥 하나 빼면된다.
비어있는데 D가 들어올 수 있음

heapq의 기본은 최소힙
=> 최소힙, 최대힙 따로 관리하고 마지막에 공통된 자원 뽑아내고 최대,최소 구하기
"""
import heapq
import sys
input = sys.stdin.readline


INF = 1000001

T = int(input())
for t in range(T):
    k = int(input())

    maxq = []
    minq = []
    visited = [0 for i in range(INF)]

    for k in range(k):
        op, num = input().split()
        num = int(num)

        if op == 'I':  # insert
            heapq.heappush(maxq, (-num, k))
            heapq.heappush(minq, (num, k))
            visited[k] = 1
        else:  # delete
            if num == 1:
                while len(maxq) > 0 and visited[maxq[0][1]] == 0:
                    _num, _k = heapq.heappop(maxq)
                if len(maxq) != 0:
                    _num, _k = heapq.heappop(maxq)
                    visited[_k] = 0
            if num == -1:
                while len(minq) > 0 and visited[minq[0][1]] == 0:
                    _num, _k = heapq.heappop(minq)
                if len(minq) != 0:
                    _num, _k = heapq.heappop(minq)
                    visited[_k] = 0

    while len(maxq) > 0 and visited[maxq[0][1]] == 0:
        _num, _k = heapq.heappop(maxq)
    while len(minq) > 0 and visited[minq[0][1]] == 0:
        _num, _k = heapq.heappop(minq)

    if len(maxq) == 0:
        print("EMPTY")

    else:
        print(-heapq.heappop(maxq)[0], end=" ")
        print(heapq.heappop(minq)[0], )
