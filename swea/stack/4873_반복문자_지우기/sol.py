import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    words = input()
    stack_words = ''

    for i in words:
        print(i)
        
