import sys
sys.stdin = open('input.txt')

T = int(input())
# 0~9 까지 숫자 적인 N장의 카드
# 가장 많은 카드에 적힌 숫자 그리고 그게 몇장인가?
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))
    count_list = [0 for i in range(10)]
    
    for number in numbers:
        count_list[number] +=1

    max_count = 0
    for idx, count in enumerate(count_list):
        # 크커나 같을떄로 한 이유는 같은 수일때도 뒤의 인덱스로 덮어 더 큰 수가 출력되도록 함을 위해
        if max_count <= count:
            result = idx
            max_count = count     

    print(f'#{tc} {result} {max_count}')