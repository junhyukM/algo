# 행우선 순회 (기존에 했던 방식)

# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12],
# ]

# 첫번째 반복문
# row_count = len(arr)
# 두번째 반복문
# column_count = len(arr[0])

# print(row_count, column_count)

# for row in range(row_count):
#     for column in range(column_count):
        # print(row, column, arr[row][column])


# 열 우선 순회
# 행 우선 순회에서 반복문 순서만 바뀜
# for column in range(column_count):
    # for row in range(row_count):
        # print(row, column, arr[row][column])
        

# 지그재그 순회
# for row in range(row_count):
#     for column in range(column_count):
        # print(arr[row][column  + (column_count-1-2*column) * (row%2)])
        ## print(arr[row][(M - column - 1) * (row%2)])


# 델타를 이용한 2차 list 탐색
# 델타 이동
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]
# LRUD
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# UDLR
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for x in range(len(arr)):
#     for y in range(len(arr[0])):
#         print(f'현재 위치는 {arr[x][y]}')

#         # 상하좌우 탐색
#         for i in range(4):
#             temp_x = x + dx[i]
#             temp_y = y + dy[i]

#             if 0 <= temp_x < len(arr) and 0 <= temp_y < len(arr[0]):
#                 print(f'{i} 방향에 있는 수는 {arr[temp_x][temp_y]}')
#             else:
#                 print(f'벽 밖의 데이터입니다 : {temp_x} {temp_y}')


# 부분집합
numbers = [2, 6, 3, 1]

n = len(numbers)

# 1을 두번씩 곱해간다 (n번만큼) => 2^4
for i in range(1<<n):
    # print(bin(i), end=', ')
    for j in range(n):
        if i & (1<<j):
            print(numbers[j], end = ', ')
    print()





