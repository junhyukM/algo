import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 10개의 0을 집어 넣는 리스트컴프리헨션
    counter = [0 for i in range(10)]
    numbers = list(map(int, input()))
    
    is_babygin = 0
    for number in numbers:
        counter[number] += 1


    idx = 0
    while idx < len(counter):    
        # 1. triplete인지 검증
        # 상위에 idx를 0으로 변수로 저장을 한 후
        # idx 값이 while문에 의해 증가해서 기존에 만들어 두었던 counter 리스트의 길이가 될 때 까지 반복
        # 만약 같은 idx (같은 숫자)에 3이상의 count값이 있다면, triplete 조건 만족
        if counter[idx] >= 3:
            # 미리 변수로 0을 저장했던 is_babygin에 1 count 플러스
            is_babygin += 1
            # 저장 했으니 3 count 마이너스
            counter[idx] -= 3
            continue

        # 2. run 검증
        # idx 기준으로 3개의 연속적인 값에 값이 있어 True를 반환하면 if문 만족
        # 그리고 세개의 연속된 숫자에 값이 있다는 뜻이므로 run 조건 만족
        # 두 칸씩 확인하기 때문에 마지막 2번은 안한다는 의미로 조건문 추가
        if idx < len(counter) - 2:
            if counter[idx] and counter[idx+1] and counter[idx+2]:
                # is_babygin count 플러스
                is_babygin += 1
                # run에 해당된 idx 들 count 하나씩 마이너스
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
                continue
        # while문 조건을 위한 idx += 1
        idx += 1
    # is_babygin 의 count가 2 라면 triplete 또는 run으로 두개의 조합을 만족한다는 뜻이므로    
    if is_babygin == 2:
        # babygin 인지 아닌지 유무를 True / False로 반환
        result = True
    else:   
        result = False        

    print(f'#{tc} {result}')

