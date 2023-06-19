import sys
# 스탠다드 인풋
# 한 줄에 하나의 데이터로 인식
sys.stdin = open('input.txt')

# 숫자데이터 하나 받아오기
N = int(input())
result = '홀수' if N % 2 else '짝수'
print(f'#1 {result}')

# 리스트 형태의 데이터 받아오기
numbers = list(map(int, input().split()))
result = sum(numbers)
print(f'#2 {result}')

# 2차원 리스트형태의 데이터 받아오기
# 3번째 줄의 3 을 이용해 아래의 4~6줄의 데이터 가져오기
number_list = []
N = int(input())
for i in range(N):
    numbers = list(map(int, input().split()))
    number_list.append(numbers)

result = number_list[1][1]
print(f'#3 {result}')

