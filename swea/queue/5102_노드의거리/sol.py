import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    nodes = []
    for _ in range(E):
        nodes.append(list(map(int, input().split())))
    S, G = map(int, input().split())

    