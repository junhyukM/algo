import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : N개의 숫자로 이루어진 수열
    # M : 뒤로 보내는 횟수
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for _ in range(M):
        deq = numbers.pop(0)
        numbers.append(deq)

    print(f'#{tc} {numbers[0]}')

