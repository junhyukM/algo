#임의의 양의 정수를 입력 받아
num = int(input())
result = []

for i in range(1, num+1):
    # 약수 확인
    if num % i == 0:
        print(f'{i}(은)는 {num}의 약수입니다.')
        # 비어있는 리스트에 약수인 수들을 append
        result.append(i)
# 반복문이 종료되고 result 리스트에 들어있는 값이 2개라면 (3개 미만) 소수        
if len(result) < 3:
    print(f'{num}(은)는 1과 {num}로만 나눌 수 있는 소수입니다.')       
