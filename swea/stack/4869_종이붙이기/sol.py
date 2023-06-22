import sys
sys.stdin = open('input.txt')

T = int(input())

# n = (n-1) + (n-2)*2
for tc in range(1, T+1):

    # 앞의 수를 활용하기 위해 임의로 넣은 값
    # 0, 10, 20 의 길이를 가질때 기본값
    memo = [0, 1, 3]

    # 10, 20, 30, 40, 50, 60....
    # 인덱스로 접근하기 위해 10으로 나눠서 몫만 취함
    N = int(input()) // 10

    while N >= len(memo):
        # 두 칸 전의 값
        p2 = memo[len(memo)-2]
        # 한 칸 전의 값
        p1 = memo[len(memo)-1]

        now = p1 + p2 * 2

        memo.append(now)

    print(memo)    
