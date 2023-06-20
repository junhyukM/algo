import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 색칠 할 영역 개수
    N = int(input())
    
    # location_color : 왼쪽 위 모서리와 오른쪽 아래 모서리의 좌표와 1 or 2 로 색상정보
    # N 에 따라 input으로 가져와야 하는 데이터의 수가 바뀌므로 그에 맞춰 반복문으로 가져옴
    color_arr = []
    for i in range(1, N+1):
        color_arr.append(list(map(int, input().split())))
    

    # 문제에서 '주어진 정보에서 같은 색인 영역은 겹치지 않는다.' 라는 지문이 있기에 같은 색은 겹치지 않는다고 보고
    # counter 영역 만들어서 색이 칠해질때마다 count를 올려 2 이상이면 보라색이라고 판단하는 방법 시도
    # 10 * 10 
    counter = []
    for row in range(10):
        row_list = []
        for column in range(10): 
            row_list.append(0)
        counter.append(row_list)    


    # 색칠하기 
    print(color_arr)
    for array in color_arr:
        for i in range(5):
            array[i]
            print(array[i])



