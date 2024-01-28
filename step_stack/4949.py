import sys
input = sys.stdin.readline

while True :
    text = list(input().rstrip())
    if text == ['.']:
        break
    vps1 = '()'
    vps2 = '[]'
    stack = []
    for j, ps in enumerate(text):
        if ps == '(' or ps == ')' or  ps == '[' or ps == ']':
            if len(stack) == 0:
                stack.append(ps)
            else:
                if stack[-1] + ps == vps1 or stack[-1] + ps == vps2:
                    del stack[-1]
                else:
                    stack.append(ps)
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
