import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 화덕의 크기 N 개의 피자를 동시에 구울 수 있음
    # M : 구워야 하는 피자의 수
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    # 반복문 안에서 일단 N 이 허용하는 만큼의 피자를 넣을 것이다
    # 각각의 피자는 치즈의양이 다르고 한바퀴씩 돌때 2분의 1로 줄어들며 정수값만 남긴다
    # 치즈가 다 녹은 피자는 꺼내고 아직 넣지 않은 피자를 넣는다
    # 이런 방식으로 피자를 구웠을때, 가장 마지막까지 남아있는 피자 번호를 알아내자
    # 피자에 번호를 매겨야한다? enumerate()을 활용해야하나 고민
    
