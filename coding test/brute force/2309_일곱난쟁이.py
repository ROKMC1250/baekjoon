import sys
import itertools
input = sys.stdin.readline
H_list = []
for i in range(9):
    H = int(input())
    H_list.append(H)
for i in itertools.combinations(H_list, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break
