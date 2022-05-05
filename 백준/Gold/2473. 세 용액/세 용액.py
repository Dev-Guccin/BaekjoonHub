"""
투포인터 + 이분탐색
arr[i] + arr[j] + arr[k]
i를 고정시키고 j,k를 투포인터처럼 활용하는 기법
"""

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
diff = 1000000000 * 3
answer = []
for i in range(len(arr)-2):

    j = i+1
    k = len(arr)-1

    while j < k:
        total = arr[i] + arr[j] + arr[k]
        if total == 0:
            print(arr[i], arr[j], arr[k])
            exit()
        if total < 0:
            if abs(diff) > abs(total):
                answer = [arr[i], arr[j], arr[k]]
                diff = total
            j += 1
        elif total > 0:
            if abs(diff) > abs(total):
                answer = [arr[i], arr[j], arr[k]]
                diff = total

            k -= 1
print(" ".join(map(str, answer)))
