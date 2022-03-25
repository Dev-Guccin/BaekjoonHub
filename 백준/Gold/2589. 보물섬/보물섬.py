"""
BFS로 최솟값을 구하지만 문제는 시작 노드를 어떻게 판별하는가?
시작 노드는 leaf노드여야한다. => 
"""


from collections import deque
R, C = map(int, input().split())
M = []

dy = [-1, 1, 0, 0]  # 상하 좌우
dx = [0, 0, -1, 1]
L = []
for i in range(R):
    tmp = list(input())
    M.append(tmp)
for i in range(R):
    for j in range(C):
        if M[i][j] == 'L':
            L.append([i, j])


def BFS(leaf):
    q = deque([leaf])

    visited = [[0 for i in range(C)] for i in range(R)]
    visited[leaf[0]][leaf[1]] = 1
    time = -1
    while q:
        time += 1
        for _ in range(len(q)):
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < R and 0 <= nx < C and M[ny][nx] == 'L' and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append([ny, nx])
    return time


answer = 0
# 리프부터 돌면서 BFS
for leaf in L:
    answer = max(answer, BFS(leaf))
print(answer)
