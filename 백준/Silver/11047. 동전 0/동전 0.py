n,k = map(int,input().split())

coin =[]
for _ in range(n):
    coin.append(int(input()))

number = 0
for ci in range(n-1,-1,-1):
    while 1:
        if coin[ci] <= k:
            number += (k//coin[ci])
            k %= coin[ci]
            continue
        else:
            break
    if k == 0:
        break
print(number)
