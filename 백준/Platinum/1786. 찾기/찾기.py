T = input()
P = input()


def kmpTable(string):

    p = 0
    tb = [0 for i in range(len(string))]
    for i in range(1, len(string)):
        # pidx가 0이 되거나 i와 stirng의 접근값이 같아질때까지 진행
        while p > 0 and string[i] != string[p]:
            p = tb[p-1]

        if string[i] == string[p]:
            p += 1
            tb[i] = p
    return tb


pi = kmpTable(P)

p = 0
n = len(T)
m = len(P)
result = []

for i in range(len(T)):

    while 0 < p and T[i] != P[p]:
        p = pi[p-1]

    if T[i] == P[p]:
        if p == m-1:  # 끝문자 인경우
            result.append(i-m+2)
            p = pi[p]
        else:  # 끝점이 아닌경우
            p += 1
print(len(result))
print(" ".join(map(str, result)))
