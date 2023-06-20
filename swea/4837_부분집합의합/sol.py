import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 1~ 12까지 숫자 원소로가진 집합 A
    # 집합 A의 부분 집합 중 원소의 수 N
    # 원소들의 합이 K 인 부분집합의 개수 출력하는 문제
    numbers = [i for i in range(1,13)]

    N, K = map(int, input().split())

    n = len(numbers)

    # 1을 두번씩 곱해간다 (n번만큼)
    for i in range(1<<n):
        set_list = []
        for j in range(n):
            if i & (1<<j):
                set_list.append(numbers[j])
            
    
            
                