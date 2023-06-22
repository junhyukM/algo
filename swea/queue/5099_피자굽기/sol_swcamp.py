import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 화덕의 크기 N 개의 피자를 동시에 구울 수 있음
    # M : 구워야 하는 피자의 수
    N, M = map(int, input().split())
    # 피자에 올려진 치즈 갯수
    cheese = list(map(int, input().split()))

    # 피자 넘버링 과정
    # before = 완성 전 피자
    before = []
    for i in range(M):
        # 치즈 갯수에 피자 넘버를 넣은 리스트들로 만들기
        before.append([cheese[i], i])
    
    # 비어있는 화덕 생성
    queue = [0] * N

    # 완성된 피자
    after = []

    # 완성된 피자가 만들어야하는 피자 갯수(M)와 같아질 때 까지 반복
    while len(after) != M:

        # 피자를 넣는 과정
        # 화덕 입구에 공간이 비었다면
        if queue[0] == 0:
            # 넣을 피자가 있는지 확인
            if len(before) != 0:
                # c : 초기 치즈값 / i : 피자 번호
                c, i = before.pop(0)
                # 피자를 화덕에 넣기
                queue.append([c, i])
                # 화덕 돌리기
                # 빈공간 하나 pop
                # 0으로 채운 N 개의 공간이 있는데, 값을 새로 넣었으므로
                # 가장 앞에 있는 0을 하나 pop해서 빼는 개념으로 보면 됨
                queue.pop(0)
            # 넣을 피자가 없다면 화덕 돌리기
            else:
                # 맨 앞 빼고
                queue.pop(0)
                # 뒤에 0 추가
                queue.append(0)
                
        # 화덕 입구에 피자가 이미 있는경우(피자를 넣을 공간이 없는 경우)
        else:
            # 치즈를 절반 감소
            queue[0][0] //= 2

            # 현재 다 완성된 피자인지 확인
            if queue[0][0] == 0:
                # 완성된 피자 꺼내기
                pizza = queue.pop(0)
                # 완성 리스트에 피자 번호 추가
                after.append(pizza[1])

                # 넣을 피자 있는지 확인
                if len(before) != 0:
                    # 남은 첫번째 피자 (c:초기치즈, i:피자번호)
                    c, i = before.pop(0)
                    # 화덕에 넣기
                    queue.append([c,i])
                else:
                    # 바로 위에서 완성된 피자 빼낸 흐름이기에 0을 빼지않고 그냥 넣기만 한다
                    queue.append(0)    

            # 아직 미완성 이라면
            else:
                # 아직 완성되지 않은 피자를 제일 뒤로 돌려주기
                pi = queue.pop(0)
                queue.append(pi)
    # 반복문을 용이하게 하기 위해 범위를 1~M-1로 했기 때문에 마지막에 1씩 플러스해서 출력하면 됨
    print(f'#{tc} {after[-1] + 1}')
