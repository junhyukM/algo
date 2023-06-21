import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    matrix = []
    for _ in range(100):
        matrix.append(list(map(int, input().split())))

    # 좌상단 => 우하단 대각선
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]

    # 우상단 => 좌하단 대각선
    total = 0
    for i in range(100):
        total += matrix[i][99-i]
