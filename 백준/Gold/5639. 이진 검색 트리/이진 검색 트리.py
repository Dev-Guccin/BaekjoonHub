import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

preorder = []
while True:
    try:
        value = int(input())
        preorder.append(value)
    except:
        break


def postOrder(first, end):
    if first > end:
        return
    mid = end+1
    for i in range(first+1, end+1):
        if preorder[first] < preorder[i]:
            mid = i
            break
    postOrder(first+1, mid-1)
    postOrder(mid, end)
    print(preorder[first])


postOrder(0, len(preorder)-1)
