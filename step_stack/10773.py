import sys
input = sys.stdin.readline

num = int(input())
stack = []

for _ in range(num):
    price = input().rstrip()
    if price == '0':
        del stack[-1]
    else:
        stack.append(int(price))

if len(stack) == 0:
    print(0)
else:
    print(sum(stack))