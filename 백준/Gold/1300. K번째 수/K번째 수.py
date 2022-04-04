import time
n = int(input())
k = int(input())
l = 1
r = n*n
m = (l+r)//2
tmp = []
while l < r:
    # calc
    #time.sleep(1)
    count = 0
    for i in range(1,n+1):
        if n*i <= m:
            count+= n
        else:
            count += m//i
    if count > k:
        r = m
    elif count < k:
        l = m + 1
    else:
        tmp.append(m)
        r = m
    m = (l+r)//2
if len(tmp) != 0:
    print(min(tmp))
else:
    print(m)
