import sys
n = int(sys.stdin.readline())

nr1 = 0
n0 = 0
n1 = 0
def check(p):
    global nr1
    global n0
    global n1
    f = p[0][0]
    wrong = 0
    for i in range(len(p)):
        for j in p[i]:
            if f != j:
                wrong = 1
                break
        if wrong == 1:
            break
    if wrong == 1:#중간에 노이즈 있으므로 나눠줘야함.
        for _ in range(0,len(p),len(p)//3):
            a=[] 
            b=[]
            c=[]
            for i in range(_, _+len(p)//3):
                a.append(p[i][:len(p)//3])
                b.append(p[i][len(p)//3:len(p)//3*2])
                c.append(p[i][len(p)//3*2:])
            check(a)
            check(b)
            check(c)
    else:
        if f == -1:
            nr1 += 1
        elif f == 0:
            n0 += 1
        else:
            n1 += 1
p = []
for _ in range(n):
    p.append(list(map(int, sys.stdin.readline().split())))
check(p)

print(nr1)
print(n0)
print(n1)