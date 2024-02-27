import sys
input = sys.stdin.readline
H_list = []
for i in range(9):
    H = int(input())
    H_list.append(H)
H_list.sort()
print(H_list)

