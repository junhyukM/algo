import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    text = input()

    s = []

    for char in text:
        if char == '(' or char == '{':
            s.append(char)

        elif char == ')':
            # 마지막 스택이 나랑 쌍이 맞다면
            if s[-1] == '(':
                s.pop()
            else:
                s.append(char)    

        elif char == '}':
            if s[-1] == '{':
                s.pop()
            else:
                s.append(char)

    if len(s) == 0:
        print(1)
    else:
        print(0)


