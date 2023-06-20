import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 정수의 개수
    # numbers : 정렬이 되지 않은 N개의 숫자 리스트
    N = int(input())
    numbers = list(map(int, input().split()))

    # 버블정렬
    for i in range(len(numbers)-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    result = []

    for i in range(5):
        # 뒤에서부터 숫자를 불러와서 append
        result.append(numbers[-i-1])
        # 앞에서부터 숫자를 불러와서 append
        result.append(numbers[i])
                    
    result = ' '.join(map(str, result))          

    print(f'#{tc} {result}')      