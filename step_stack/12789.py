import sys
input = sys.stdin.readline

num = int(input())
order = list(map(int,input().split()))

# stack = []
# result = 1

# while result != num + 1 :
#     if len(order) != 0:
#         if result == order[0]:
#             result += 1
#             del order[0]
#         elif (len(stack) != 0) and (stack[-1] == result):
#             result += 1
#             del stack[-1]
#         elif len(order) >= 0:
#             stack.append(order[0])
#             del order[0]
#         else:
#             print('Sad')
#             break
#     else:
#         if (len(stack) != 0) and (stack[-1] == result):
#             result += 1
#             del stack[-1]
#         else:
#             print('Sad')
#             break

# if len(stack) == 0:
#     print('Nice')
result = 1
stack = []
for i in order:
    if i == result:
        result += 1
    else:
        stack.append(i)
    while stack:
        if stack[-1] == result:
            del stack[-1]
            result += 1
        else:
            break
if len(stack) == 0:
    print('Nice')
else:
    print('Sad')