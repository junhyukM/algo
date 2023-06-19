import sys
sys.stdin = open('input.txt')

T = int(input())
# 0~9 까지 숫자 적인 N장의 카드
# 가장 많은 카드에 적힌 숫자 그리고 그게 몇장인가?
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))
 
    counter = [0 for i in range(10)]

    for number in numbers:
        counter[number] += 1
    
    idx = 0
   
