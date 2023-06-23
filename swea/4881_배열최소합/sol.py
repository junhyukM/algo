import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    # N : N x N 의 배열이 주어진다
    N = int(input())
    array = []
    for _ in range(N):
        array.append(list(map(int, input().split())))

    # 백트래킹을 해야하는 문제이기 때문에 함수를 사용해야한다.(재귀)
    # 이미 지나간 길이라는 기록을 stack을 해놓을 리스트 필요
    # 최소합 변수가 있고, 조건문에 따라 최소합을 갱신하는 함수 작성 필요
    def backtrack():
        pass
    

