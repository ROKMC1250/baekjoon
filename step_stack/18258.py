import sys
from collections import deque
input = sys.stdin.readline

num = int(input())
queue = deque([])
for _ in range(num):
    command = input().rstrip().split()
    if command[0] == 'push':
        integer = command[1]
        queue.append(integer)
    if command[0] == 'pop':
        print(queue.popleft()) if (len(queue) != 0) else print(-1)
    if command[0] == 'size':
        print(len(queue))
    if command[0] == 'empty':
        print('1') if (len(queue) == 0) else print(0)
    if command[0] == 'front':
        print(queue[0]) if (len(queue) != 0) else print(-1)
    if command[0] == 'back':
        print(queue[-1]) if (len(queue) != 0) else print(-1)
