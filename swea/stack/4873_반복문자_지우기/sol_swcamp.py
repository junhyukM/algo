import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    string = input()
    
    stack = []
    
    for char in string:
        # 스택이 비어있는경우
        if len(stack) == 0:
            stack.append(char)
        # 스택에 데이터가 있는경우
        else:
            # 스택의 제일 마지막 데이터가 지금 반복문을 돌고있는 데이터와 일치하면
            if stack[-1] == char:
                stack.pop()
            # 일치하지 않는다면
            else:
                stack.append(char)

    print(f'#{tc} {len(stack)}')            
