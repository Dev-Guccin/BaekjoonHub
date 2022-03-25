"""
3
3
0 1 0
1 0 1
0 1 0
1 2 3

"""

N = int(input())
M = int(input())
parent = [i for i in range(N+1)]


def find(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, A, B):
    A = find(parent, A)
    B = find(parent, B)

    if A < B:
        parent[B] = A
    else:
        parent[A] = B


for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            union(parent, i, j+1)

citys = list(map(int, input().split()))

# 같은 부모를 가지는지 확인한다.
p = parent[citys[0]]
for city in citys:
    if parent[city] != p:
        print("NO")
        exit(0)
print("YES")
