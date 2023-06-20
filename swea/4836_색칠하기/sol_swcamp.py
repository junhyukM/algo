import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 색칠 할 영역 개수
    N = int(input())

    # 0으로 채워진 리스트 생성
    board = [[0 for _ in range(10)] for _ in range(10)]
    # pprint(board)

    for i in range(N):
        color_data = list(map(int, input().split()))
    
        left_top_x = color_data[0]
        left_top_y = color_data[1]
        right_bottom_x = color_data[2]
        right_bottom_y = color_data[3]

        color = color_data[4]

        # 색칠하는 코드
        for x in range(left_top_x, right_bottom_x + 1):
            for y in range(left_top_y, right_bottom_y + 1):
                board[x][y] += color

    count = 0
    for x in range(10):
        for y in range(10):
            if board[x][y] == 3:
                count += 1

    pprint(f'#{tc} {count}')
