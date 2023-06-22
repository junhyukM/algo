import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 전체 보드의 길이
    # M : 파리채 길이
    N, M = map(int, input().split())

    matrix = [list(map(int,input().split())) for i in range(N)]
    
    result = 0
    # N-M+1 => 기준점이 반복문을 돌 수 있는 범위
    for i in range(N-M+1):
        for j in range(N-M+1):
            # print(matrix[i][j]) = > 기준점
            # 파리채 크기(M x M)만큼 반복을 돌면서 총 합
            temp_total = 0
            for col in range(M):
                for row in range(M):
                    #나의 현재 위치
                    temp_total += matrix[i+col][j+row]

            if result < temp_total:
                result = temp_total

    print(f'#{tc} {result}')            