import sys
sys.stdin = open('input.txt')


for tc in range(10):
    # N : 건물 개수
    N = int(input())

    numbers = list(map(int, input().split()))
    
    jomang_list = []
    # 양쪽 두개씩 0으로 채운다고 했으니 range 범위 설정
    for i in range(2, N-2):
        result = 0
        jomang = []
        # 좌우 2칸씩의 조망 계산
        for j in range(3):
            if numbers[i] - numbers[i+j] > 0:
                # 오른쪽 조망가능 칸 수
                jomang.append(numbers[i] - numbers[i+j])
                
            if numbers[i] - numbers[i-j] > 0:    
                # 왼쪽 조망가능 칸 수
                jomang.append(numbers[i] - numbers[i-j])
            else:
                continue
            print(jomang)

            min_jomang = min(jomang)

        result += min_jomang

    print(result)         

