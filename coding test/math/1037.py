import sys
input = sys.stdin.readline
num = int(input().rstrip())
num_list = sorted(list(map(int, input().rstrip().split())))
# num_list = list(map(int, input().rstrip().split()))
# min = min(num_list)
# max = max(num_list)
# print(min * max)
if len(num_list)%2 == 0:
    print(num_list[0] * num_list[-1])
else:
    print(num_list[len(num_list)//2]**2)