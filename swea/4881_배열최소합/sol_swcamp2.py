import sys
sys.stdin = open('input.txt')

# 모든 경우의 수를 찾는 함수 만들기
def search(index, visited, SUM):
    global MIN

    if index >= N:
        if SUM < MIN:
            MIN = SUM
        return
    
    # 함수가 진행되는 중간값이 이미 MIN을 넘어서는 경우엔 가지치기로 그냥 끝내버린다
    if SUM > MIN:
        return

    for i in range(0,N):
        if visited[i] == False:

            # result.append(numbers[index][i])
            SUM += numbers[index][i]
            visited[i] = True
            search(index+1, visited, SUM)
            visited[i] = False
            # result.pop()
            SUM -= numbers[index][i]



T = int(input())
for tc in range(1, T+1):
    # N : N x N 의 배열이 주어진다
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(list(map(int, input().split())))

    visited = [False] * N
    MIN = 99999999999999
    SUM = 0


    search(0, visited, SUM)
    print(f'#{tc} {MIN}')