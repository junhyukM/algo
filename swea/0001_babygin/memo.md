# 문제 내용 및 해결과정 정리


### 1. 조합하는 대상이 0 ~ 9 라는 정해진 범위 안에서 다루어지는 부분
### 2. while 반복문을 사용하고, idx(조회 위치)의 값을 원하는 만큼 수정하는 부분, 반복문이 종료가 되는 조건
### 3. baby gin 을 만족하는 조건을 is_babygin 의 count를 이용
### > 10개의 0으로 채워진 counter 리스트를 생성 -> 0~9 숫자의 count를 채워 넣음 -> idx = 0으로 해놓고 while 반복문 작성 -> idx < len(counter) 가 참인 동안 반복 -> 같은 수가 세번 나왔다면 count가 3 이상이라는 조건문으로 확인, is_babygin count중가, counter[idx] 수정 -> 연속된 세 idx, idx+1, idx+2 위치가 True(값이 있음)를 반환하면 run의 조건을 만족, is_babygin, counter[idx] 수정 -> is_babygin 가 2인지 확인 후 True / False 반환


### 같은 내용 연습에 사용 가능하도록 주석만 작성, 복사하여 사용
```python
    # 10개의 0을 집어 넣는 리스트컴프리헨션
        # 1. triplete인지 검증
        # 상위에 idx를 0으로 변수로 저장을 한 후
        # idx 값이 while문에 의해 증가해서 기존에 만들어 두었던 counter 리스트의 길이가 될 때 까지 반복
        # 만약 같은 idx (같은 숫자)에 3이상의 count값이 있다면, triplete 조건 만족
            # 미리 변수로 0을 저장했던 is_babygin에 1 count 플러스
            # 저장 했으니 3 count 마이너스

        # 2. run 검증
        # idx 기준으로 3개의 연속적인 값에 값이 있어 True를 반환하면 if문 만족
        # 그리고 세개의 연속된 숫자에 값이 있다는 뜻이므로 run 조건 만족
        # 두 칸씩 확인하기 때문에 마지막 2번은 안한다는 의미로 조건문 추가
                # is_babygin count 플러스
                # run에 해당된 idx 들 count 하나씩 마이너스
        # while문 조건을 위한 idx += 1
    # is_babygin 의 count가 2 라면 triplete 또는 run으로 두개의 조합을 만족한다는 뜻이므로    
        # babygin 인지 아닌지 유무를 True / False로 반환
```
