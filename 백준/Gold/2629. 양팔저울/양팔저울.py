"""
주어진 추만으로 구슬의 무게를 확인할 수 있는지결정하는 프로그램

2 : 추의 개수 <= 30
1 4 : 추의 무게들 (오름차순)
2 : 구슬 개수 <= 7
3 2 : 구슬들의 무게(무게<=40,000)

collections로 모든 경우의 수 구하는건 경우의 수가 많아서 불가능
완탐으로 구해놓고 메모이제이션 해야한다.
"""

N = int(input())
W = list(map(int, input().split()))

M = int(input())
Marble = list(map(int, input().split()))

P = [0 for i in range(40000+1)]
dp = [[False for i in range(500*(N+1)+1)] for i in range(N+1)]


def recur(index, total):
    global N
    global W
    # 탈출조건
    if index > N:
        return
    # set을 적용하듯이 중복된 조건은 제외시켜버린다. 백트래킹이나 DFS를 재귀로 풀어내야할떄 dp를 N차로 바꾸어 활용하는 경우 좋을 거 같다.
    if dp[index][total]:
        return
    dp[index][total] = True

    # 사용할건지 안할건지
    recur(index+1, total)  # 사용안함
    recur(index+1, total+W[index-1])  # 사용함
    recur(index+1, abs(total-W[index-1]))  # 사용함


recur(0, 0)

for m in Marble:
    if m > 30*500:
        print("N")
        continue
    if dp[N][m]:
        print("Y")
    else:
        print("N")
