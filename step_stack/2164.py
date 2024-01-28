import sys
from collections import deque
input = sys.stdin.readline
num = int(input())
stack = deque([i + 1 for i in range(num)])
i = 0
while len(stack) != 1:
    if (i+1) % 2 == 0:
        stack.append(stack.popleft())
    else:
        del stack[0]
    i += 1
print(stack[0])

# stack = deque([i*2 for i in range(1, num//2 + 1)])
# if num%2 == 0:
#     i = 2
# else:
#     i = 1
# while len(stack) != 1:
#     if i%2 == 0:
#         del stack[0]
#     elif i%2 != 0:
#         stack.append(stack.popleft())
#     i += 1
# print(stack[0])