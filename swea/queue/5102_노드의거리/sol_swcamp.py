import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    nodes = [[0] * (V+1) for _ in range(V+1)]
    
    for line in range(E):
        start, end = list(map(int, input().split()))
        # 양쪽 방향으로 다 오갈수 있어서 대각선을 기준으로 대칭인 형태
        nodes[start][end] = 1
        nodes[end][start] = 1

    # S : 확인을 해야하는 출발 노드
    # G : 연결되어있음을 확인하는 도착노드
    S, G = map(int, input().split())

    # 방문 체크리스트
    check_list = [False] * (V+1)
    # 거리계산을 위한 리스트
    distance = [0] * (V+1)
    # bfs 처리용 queue
    queue = []

    # v 부터 시작
    v = S
    check_list[v] = True
    queue.append(v)

    # bfs 시작
    while len(queue):
        v = queue.pop(0)
        # v와 연결된 노드 찾기
        for w in range(V+1):
            # v와 연결된 w 찾기
            if nodes[v][w] == 1:
                # 만약 아직 방문하지 않았다면
                if check_list[w] == False:
                    # 방문 처리
                    check_list[w] == True
                    # 현재 깊이에서 1 증가 시킨 후 다음 위치의 깊이 저장
                    distance[w] = distance[v] + 1 
                    queue.append(w)

    print(distance[G])






    