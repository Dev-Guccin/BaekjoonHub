adj = {}

N = int(input())


for i in range(N):
    A, B, C = input().split()
    if A not in adj:
        adj[A] = [B, C]

# 전위 순회 [root, left, right]


def recur(node, order):
    if node == '.':
        return

    left, right = adj[node]
    if order == 1:
        print(node, end="")
    recur(left, order)
    if order == 2:
        print(node, end="")
    recur(right, order)
    if order == 3:
        print(node, end="")


recur('A', 1)
print()
recur('A', 2)
print()
recur('A', 3)
print()
