import sys
sys.stdin = open('input.txt')

T = int(input())

# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이 출력
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    # 가장 큰 수와 가장 작은 수 구하기
    # 수 비교로 정렬해서 가장 앞 수와 가장 뒷 수 구하면 됨
    numbers.sort()

    max_num = numbers[-1]
    min_num = numbers[0]
    result = max_num - min_num

    print(f'#{tc} {result}')

### 강사님 풀이
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
    
#     # min_number = numbers[0]
#     min_number = 1000000
#     # max_number = numbers[0]
#     max_number = 1

#     for number in numbers:
#         if min_number > number:
#             min_number = number

#         if max_number < number:
#             max_number = number    
#     result = max_number - min_number

#     print(f'#{tc} {result}')