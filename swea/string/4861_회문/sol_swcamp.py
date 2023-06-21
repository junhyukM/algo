import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : N x N 보드
    # M : 회문의 길이
    N, M = list(map(int, input().split()))
    
    # 글자판 
    string_map = []
    for str in range(N):
        # str_input = input().split()
        string_map.append(input())

    result = ''

    # 가로
    for row in range(N):
        # print(string_map[row])
        # 회문의 시작점만 반복
        for i in range(N - M + 1):
            # print(string_map[row][i])
            # 회문인지 아닌지 확인
            # M 을 2로 나눈 몫만큼 돌리는 이유는 대칭적으로 어차피 앞뒤나 뒤앞이나 같은 내용이라 계산 줄이기 위해
            # 그냥 M으로 작성해도 상관없다
            for j in range(M//2):
                # front : 앞글자
                f = string_map[row][i+j]
                # back : 뒷글자
                b = string_map[row][i+M-j-1]
                
                # 앞뒤가 똑같다면
                if f == b:
                    flag = True
                # 앞뒤가 다르다면
                else:
                    flag = False
                    break
            # 회문을 찾음
            if flag:
                for k in range(M):
                    result += string_map[row][i+k]

    # 세로
    for column in range(N):
        for i in range(N - M + 1):
            # print(string_map[column])
            # 회문인지 아닌지 확인
            for j in range(M):
                # front : 앞글자
                f = string_map[i+j][column]
                # back : 뒷글자
                b = string_map[i+M-j-1][column]
                
                # 앞뒤가 똑같다면
                if f == b:
                    flag = True
                # 앞뒤가 다르다면
                else:
                    flag = False
                    break
            # 회문을 찾음
            if flag:
                for k in range(M):
                    result += string_map[i+k][column]                

    print(f'#{tc} {result}')
