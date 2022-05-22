"""
데터가 작고 K가 10 이하이므로
완탐으로 풀린다. 따라서 BFS로 매번 모든 경우를 찾고 해당 값 중에 가장 큰것을 선택하여 갱신
매번 최대를 구하는게 아니라 K번실행하는 경우의 최댓값을 구해야한다.
"""
from collections import deque

N, K = input().split()
N = list(N)
K = int(K)
_N = list(N)
answer = 0


def BFS(k, start):

    q = deque([int("".join(start))])
    count = 0
    while q:
        if count == k:
            return max(q)
        setq = set()
        for _ in range(len(q)):
            target = q.popleft()
            target = list(str(target))
            for i in range(len(N)):
                for j in range(i+1, len(N)):
                    tmp = list(target)
                    tmp[i] = target[j]
                    tmp[j] = target[i]
                    if tmp[0] == '0':
                        continue
                    setq.add(int("".join(tmp)))
        q += (list(setq))
        count += 1


tmp = BFS(K, _N)
if tmp == None:
    print(-1)
else:
    print(tmp)
