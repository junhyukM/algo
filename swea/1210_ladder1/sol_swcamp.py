import sys
sys.stdin = open('input.txt')

T = 10
# 10개의 테스트 케이스
for _ in range(1, T+1):
    # 테스트 케이스가 데이터에 하나하나 명시되어 있어 내부에서 input()
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if ladder[99][i] == 2:
            # x, y는 현재 내 위치 (도착 지점)
            x = i
            y = 99

    # y가 0이 되는 순간 = 가장 윗줄 = 도착했다는 뜻
    while y > 0:
        # 현재 위치를 기준으로 좌우를 체크
        
        # 제일 오른쪽과 제일 왼쪽이 아니라면(아웃 오브 레인지를 방지하기 위해) => 좌우를 살펴보세요
        if x != 99 and x != 0:
            # 왼쪽을 보는 경우
            if ladder[y][x-1] == 1:
                # 원래 있던 자리를 0으로 바꾸고
                ladder[y][x] = 0
                # 왼쪽으로 한 칸 간다
                x -= 1
                continue
            # 오른쪽을 보는 경우
            if ladder[y][x+1]:
                ladder[y][x] = 0
                x += 1
                continue

        # 제일 오른쪽이라면 => 왼쪽만 살펴보세요
        elif x == 99:
            if ladder[y][x-1] == 1:
                ladder[y][x] = 0
                x -= 1
                continue

        # 제일 왼쪽이라면 => 오른쪽만 살펴보세요
        elif x == 0:
            if ladder[y][x+1]:
                ladder[y][x] = 0
                x += 1
                continue

        ladder[y][x] = 0
        y -= 1

    result = x
    print(f'#{tc} {x}')       

