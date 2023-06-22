import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    words = list(map(str, input()))
    
    word_list = []
    target = ['(', ')', '{', '}']
    
    # append로 target에 맞는 문자열들 word_list 리스트에 추가
    for i in words:
        for j in target:
            if i == j:
                word_list.append(i)
    
                
    print(word_list)             
