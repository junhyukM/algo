# 문제 내용 및 해결과정 정리


### 1. 문제에서 주는 변수에 대한 이해와 내용정리를 정확하게 해야함
### 2. 당장 for문을 쓸까 while문을 쓸까 같이 습관적인 생각을 하기보단 문제가 설명하는 내용의 흐름을 제대로 파악하는 노력이 필요함
### 3. 풀이에서 cnt 라던지 now 라던지 새로운 변수를 설정하는 상황에 대해 많은 연습으로 숙달이 필요함
### 4. 반복문을 사용해서 적절한 결과를 만들어 내는 연습 필요
### > 


---
### 같은 내용 연습에 사용 가능하도록 주석만 작성, 복사하여 사용
```python
import sys
sys.stdin = open('input.txt')

T = int(input())

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
```