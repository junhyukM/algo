import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # P : 전체 페이지 수
    # A : A가 찾아야 하는 페이지
    # B : B가 찾아야 하는 페이지 
    P, A, B = map(int, input().split())

    
    count_a = 1
    left = 1
    right = P
    # 언제 종료가 되는지 알 수 없기 때문에 True로 설정하고 진행
    while True:
        middle = int((left+right)/2)

        # 목적페이지가 가운데보다 왼쪽에 있는경우
        if A < middle:
            right = middle
        # 목적페이지가 가운데보다 오른쪽에 있는경우
        elif middle < A:
            left = middle
        # 둘 다 아니라면 목적페이지에 도착
        else:
            break

        count_a += 1

    count_b = 1
    left = 1
    right = P
    while True:
        middle = int((left+right)/2)

        if B < middle:
            right = middle
        elif middle < B:
            left = middle
        else:
            break

        count_b += 1

    if count_a > count_b:
        winner = 'B'
    elif count_a < count_b:
        winner = 'A'
    else:
        winner = 0

    print(f'#{tc} {winner}')        
