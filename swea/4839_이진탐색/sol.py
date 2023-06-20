import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # P : 전체 페이지 수
    # A : A가 찾아야 하는 페이지
    # B : B가 찾아야 하는 페이지 
    P, A, B = map(int, input().split())
    
    book = [i for i in range(1, P+1)]
    start_page = 1
    
    # 반복문이 끝나는 조건 설정이 어렵다
    while start_page < P:
        # 중간 값?
        mid_page = (start_page + P) // 2
        # A 와 B에 대해 동시에 만족하는 논리 구성이 어렵다.
        # 그냥 A가 만족하냐마냐로 접근하면 가능할 것 같은데 B를 같이 신경쓰려니까 어떤식으로 진행해야하나
        # 감을 잡기가 쉽지 않음
        if book[mid_page] > A:
            pass

