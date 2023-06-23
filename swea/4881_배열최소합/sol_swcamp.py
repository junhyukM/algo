import sys
sys.stdin = open('input.txt')

# 모든 경우의 수를 찾는 함수 만들기
def search(index, visited):
    global result

    if index >= N:
        print(result)

    for i in range(0,N):
        if visited[i] == False:

            result.append(numbers[index][i])
            visited[i] = True
            search(index+1, visited)
            visited[i] = False
            result.pop()



T = int(input())
for tc in range(1, T+1):
    # N : N x N 의 배열이 주어진다
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(list(map(int, input().split())))

    visited = [False] * N
    result = []

    # False로 가득한 visited 리스트를 함수에 인자로 넣는 방식으로 동작
    search(0, visited)
    print('----------')
