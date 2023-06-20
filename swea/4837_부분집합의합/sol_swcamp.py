import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 1~ 12까지 숫자 원소로가진 집합 A
    # N : 길이
    # K : 합
    N, K = map(int, input().split())

    # arr = [1, 2, 3, .... 12]
    arr = [i for i in range(1,13)]
    count = 0
    for i in range(1 << len(arr)):
        result = []
        for j in range(len(arr)):
            if i & (1 << j):
                result.append(arr[j])
        # 모든 부분집합 출력        
        if len(result) == N and sum(result) == K:
            count += 1

    print(f'#{tc} {count}')