import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # V : 노드 수
    # E : 간선 수
    V, E = list(map(int, input().split()))

    # 노드 번호는 1부터 시작하기 때문에 V+1 (인덱스로 조회하는 것을 용이하게 하기 위해)
    # 모두 0으로 채우기
    nodes = [[0]*(V+1) for _ in range(V+1)]

    # 간선 수 만큼 가져오기
    for line in range(E):
        start, end = list(map(int, input().split()))
        # nodes에 값 넣어주기
        nodes[start][end] = 1
    # 위의 부분이 그래프를 그린 과정

    # S 부터 시작해서 G 까지 갈 수 있는지 확인해야한다.    
    # S : 확인을 해야하는 출발 노드
    # G : 연결되어있음을 확인하는 도착 노드
    S, G = list(map(int, input().split()))    
    
    # dfs를 하기 위해 과거를 기록하는 stack 만들기
    stack = []

    # 내가 방문했던 기록을 남기는 체크리스트 만들기
    check_list = [False] * (V+1)

    # v는 현재위치
    v = S
    # 거기 있으니 기록하려 True 그리고 stack에 추가
    check_list[v] = True
    stack.append(v)

    result = 0
    while len(stack):
        # stack이 비워질 때가지 반복
        
        # 현재 나의 노드(v)와 연결된 노드(w)를 탐색
        for w in range(V+1):
            if nodes[v][w] == 1:
                # 아직 방문을 안했다면
                if not check_list[w]:
                    # 연결된 노드(w)를 방문처리
                    check_list[w] = True
                    # 나의 노드(v)를 stack에 push
                    stack.append(v)

                    # 현재위치를 이동 (v => w)
                    v = w

                    # 경로에 목적지가 있으면 저장
                    if w == G:
                        result = 1

                    break    

        # for 문을 다 돌고 else 문을 만났을 때
        # 이전 위치로 돌아가야 한다
        else:
            v = stack.pop()            

    print(f'#{tc} {result}')
