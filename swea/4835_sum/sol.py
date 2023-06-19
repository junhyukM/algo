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
    # print(N, M, numbers)
    max_sum = 0
    min_sum = 0
    # 반복문을 돌려야 하는데
    # 처음꺼부터 M 구간까지를 더하는 반복문
    # 순차적으로 마지막까지 기준점을 옮겨가는 반복문
    
                
            

            

    


 
    result = max_sum - min_sum
    print(f'#{tc} {result}')


   
