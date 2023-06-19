import sys
sys.stdin = open('input.txt')

T = int(input())

# M개의 합이 가장 큰 경우
# M개의 합이 가장 작은 경우
# 가장 큰 경우와 가장 작은 경우의 차를 구해라
for tc in range(1, T+1):
    # N : 정수의 개수, 배열의 총 개수
    # M : 구간의 개수, M개의 이웃한 수를 더한다
    N, M = map(int, input().split())
    # N 개로 이루어진 배열 데이터
    numbers = list(map(int, input().split()))
  
    # min_number = sum(numbers)
    # min_number = 100000000
    min_number = 9999999999999
    max_number = 0

    # 구간합의 시작점을 찾는 i
    for i in range(N-M+1):
        # 시작점을 기준으로 오른쪽 M개의 합
        total = 0
        for j in range(M):
            total += numbers[i+j]
        
        if total < min_number:
            min_number = total 
        if total > max_number:
            max_number = total        
    result = max_number - min_number

    print(f'#{tc} {result}')