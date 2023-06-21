import sys
sys.stdin = open('input.txt')

# 내가 제일 큰가?
# 크다면, 나를 제외한 나머지중 가장 큰 건물은 무엇인가?
T = 10
for tc in range(1, T+1):
    # N : 건물 개수
    building_num = int(input())
    building_list = list(map(int, input().split()))
    
    total = 0
    # 모든 건물들을 기준으로 반복
    for i in range(building_num):
        now = building_list[i]
        # 지금 내 위치가 0이면 비교의 의미가 없기때문에 넘기기
        if now == 0:
            continue
        # 나의 위치가 0이 아니라면 비교 시작
        else:

            # 양옆 * 2개의 건물을 비교 
            # idx를 설정해서 인덱스값 참조에 사용
            idx = [-2, -1, 1, 2]
            max_tall = 0
            # idx[j] => -2, -1, 1, 2 로 들어감
            # 양쪽 네개의 건물중 가장 큰 건물을 max_tall에 저장
            for j in range(4):
                comp = building_list[i+idx[j]]
                if max_tall < comp:
                    max_tall = comp

            if now > max_tall:
                view = now - max_tall
                total += view
    
    print(f'#{tc} {total}')

