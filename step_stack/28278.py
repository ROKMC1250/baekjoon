import sys
input = sys.stdin.readline

stack = []
num = int(input())

for _ in range(num):
    command = input().rstrip()
    if len(command) > 2:
        stack.append(int(command.split(' ')[1]))
    else:
        if command == '2':
            if len(stack) != 0:
                last = stack.pop(-1)
                print(last)
            else:
                print(-1)
        elif command == '3':
            print(len(stack))
        elif command == '4':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif command == '5':
            if len(stack) != 0:
                print(stack[-1])
            else:
                print(-1)