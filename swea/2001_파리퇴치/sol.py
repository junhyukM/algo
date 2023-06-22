import sys
from pprint import pprint

sys.stdin = open('input.txt')

T = int(input())



for tc in range(1, T+1):
    # N 파리 영역 N x N
    # M 파리채 크기 M x M
    N, M = map(int, input().split())
    # paris 파리의 마리수
    paris = []
    for n in range(N):
        paris.append(list(map(int, input().split())))
    
    # range 범위는 N-M+1
    # row를 M만큼의 간격으로 늘어나게 해야하나..?
    # for row in range(N-M+1):
    #     # 가로 덧셈
    #     for i in range(N-M+1):
    #         for j in range(M):
                



    