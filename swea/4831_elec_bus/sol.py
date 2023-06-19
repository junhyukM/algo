import sys
sys.stdin = open('input.txt')

T = int(input())

# 노선 수 T
# 각 노선별 K = 한번 충전 최대 이동 가능 정류장 수
# N = 0번에서 출발해 종점인 N번 정류장 까지 이동(종점 정류장까지 걸리는 정류장 수)
# M = 충전기가 설치된 정류장 번호
# 최소한 몇번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램
# idx = 0
# count = 0
# for tc in range(1, T+1):
#     numbers_KNM = list(map(int, input().split()))
#     numbers_M = list(map(int, input().split()))
#     # N 만큼의 0으로 채워진 카운터 리스트 생성
#     counter = [0 for i in range(numbers_KNM[1]+1)]
#     # 각 input 데이터에 정류장이 있는 위치 인덱스 1로 채우기
#     for number in numbers_M:
#         counter[number] += 1

#     # K 칸 이동이 가능한데 딱 K칸에 정류장이 있다면 거기로 이동
#     # 아니라면 인덱스를 마이너스를 해서 있으면 이동
#     while idx < len(counter):
#         if idx < len(counter) - numbers_KNM[0]:
#             for i in range(numbers_KNM[0]-2):
#                 if counter[idx + numbers_KNM[0]] == counter[numbers_KNM[1]]:
#                     idx += numbers_KNM[0]
#                 elif counter[idx + numbers_KNM[0] - i]:
#                     count += 1
#                     idx += (numbers_KNM[0] - i)
#                 else:
#                     result = 0    
# print(count)    

## 강사님 풀이

for tc in range(1, T+1):
    # K : 최대로 이동 가능한 정류장 수
    # N : 종점
    # M : 충전기가 설치된 정류장 수
    # K,N,N 각각 할당
    K, N, M = map(int, input().split())

    bus_stop = list(map(int, input().split()))
    cnt = 0
    now = 0
    # print(K, N, M, bus_stop)

    # 충전할 필요없이 바로 도착하는 경우
    if K >= N:
        cnt = 0
    # 충전하면서 지나가야 할 때
    else:
        # 버스가 아직 종점에 도착하지 않았다면 계속해서 반복
        while now < N:
            # 현재 위치(now)에서 최대로 갈 수 있는 범위(now+K)를 찾는다.
            # 최대로 갈 수 있는 범위(now+K)부터 현재위치(now) 까지 반복
            for i in range(now + K, now, -1):
                # 1. 최대범위가 종점을 넘는 경우
                if i >= N:
                    now = N
                    break
                # 2. 최대범위가 종점을 아직 넘지 않는경우
                if i in bus_stop:
                    # 가장 뒤에있는 충전소로 이동
                    now = i
                    # 충전을 하고 이동을 했으니 카운트 증가
                    cnt += 1
                    break

            # 현재 위치에서 최대 거리를 찾았는데, 충전소가 없으면? 도착 불가능
            else:
                cnt = 0
                now = N
    print(f'#{tc} {cnt}')






