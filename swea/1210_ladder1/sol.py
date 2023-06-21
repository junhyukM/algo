import sys
sys.stdin = open('input.txt')

# 10개의 테스트 케이스
for tc in range(10):
    # 테스트 케이스가 데이터에 하나하나 명시되어 있어 내부에서 input()
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 마지막 줄에 2가 있나 확인
    # print(ladder[99])

    # 여러개의 시작지점에서 출발하는 것은 비효율적
    # 도착 지점(2)에서 위로 연결된 하나의 지점을 찾아가는게 빠를듯
    
    # 이동을 할 때 특징?
    # 위로 올라가는건 좌 또는 우에 1을 만났을 때 멈추고 방향 전환
    # 좌 또는 우방향 진행은 0을 만났을 때 멈추고 위로 방향 전환
    # while 문으로 조건부로 계속 진행하게끔 하면 될 듯
    

    




