import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : N 개의 글자 N 개의 줄 -> N * N 정사각형의 단어 글자판
    # M : M 개의 글자수로 이루어진 회문을 찾는다
    # 회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
    N, M = map(int, input().split())
    
    # 글자판 
    words = []
    for i in range(N):
        words.append(list(input()))

    # 회문 여부 확인하기 (가로방향)
    count = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            palindrome = []
            for w in range(M):
                if words[j+w] == words[j+M-w]:
                    palindrome.append(words[j])
                if words[j:j+M] == palindrome:
                    result = palindrome
        print(result)        

            






