import sys
from pprint import pprint
sys.stdin = open('input.txt')


for test in range(10):
    tc = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))

    max_sum = 0     
    # row 방향들의 합 중 가장 큰 값
    for i in range(100):
        sum_row = 0
        for j in range(len(arr[i])):
            sum_row += arr[i][j]
        if sum_row > max_sum:
            max_sum = sum_row
    # column 방향들의 합 중 가장 큰 값 
    for i in range(100):
        sum_column = 0
        for j in range(len(arr[i])):
            sum_column += arr[j][i]
        if sum_column > max_sum:
            max_sum = sum_column
    # 왼쪽 위 -> 오른쪽 아래 대각선의 합
    for i in range(100):
        if max_sum < arr[i][i]:
            max_sum = arr[i][i]
    # 오른쪽 위 -> 왼쪽 아래 대각선의 합
    for i in range(100):
        if max_sum < arr[i][99-i]:
            max_sum = arr[i][99-i]       
 
    print(f'#{tc} {max_sum}')