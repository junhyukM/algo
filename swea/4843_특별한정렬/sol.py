import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 정수의 개수
    # numbers : 정렬이 되지 않은 N개의 숫자 리스트
    N = int(input())
    numbers = list(map(int, input().split()))
    

    for i in range(len(numbers)- 1):
        min_idx = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    result = []
    for i in range(len(numbers)):
        result.append(numbers[-i-1])
        result.append(numbers[i])

    result = result[:10]

    print(f'#{tc} {result}')    


        
