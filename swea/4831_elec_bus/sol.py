import sys
sys.stdin = open('input.txt')

T = int(input())

# 노선 수 T
# 각 노선별 K = 한번 충전 최대 이동 가능 정류장 수
# N = 0번에서 출발해 종점인 N번 정류장 까지 이동(종점 정류장까지 걸리는 정류장 수)
# M = 충전기가 설치된 정류장 번호
# 최소한 몇번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램

idx = 0
count = 0
for tc in range(1, T+1):
    numbers_KNM = list(map(int, input().split()))
    numbers_M = list(map(int, input().split()))
    # N 만큼의 0으로 채워진 카운터 리스트 생성
    counter = [0 for i in range(numbers_KNM[1]+1)]
    # 각 input 데이터에 정류장이 있는 위치 인덱스 1로 채우기
    for number in numbers_M:
        counter[number] += 1

    # K 칸 이동이 가능한데 딱 K칸에 정류장이 있다면 거기로 이동
    # 아니라면 인덱스를 마이너스를 해서 있으면 이동
    while idx < len(counter):
        if idx < len(counter) - numbers_KNM[0]:
            for i in range(numbers_KNM[0]-2):
                if counter[idx + numbers_KNM[0]] == counter[numbers_KNM[1]]:
                    idx += numbers_KNM[0]
                elif counter[idx + numbers_KNM[0] - i]:
                    count += 1
                    idx += (numbers_KNM[0] - i)
                else:
                    result = 0    
print(count)    