import sys
input = sys.stdin.readline

num = int(input())
vps = '()'

for i in range(num):
    stack = []
    test = list(input().rstrip())
    for j, ps in enumerate(test):
        if len(stack) == 0:
            stack.append(ps)
        else:
            if stack[-1] + ps == vps:
                del stack[-1]
            else:
                stack.append(ps)
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

