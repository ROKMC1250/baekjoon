import sys
input = sys.stdin.readline
N = int(input())
jump = list(map(int,input().rstrip().split()))
DP = [- 1] * N
DP[0] = 0

for current in range(0, N - 1):
    # print('------------------')
    # print('current', current)
    if DP[current] == -1:
        print(-1)
        break
    for next_step in range(1, jump[current] + 1):
        if current + next_step >= N:
            break
        # print('next_step', next_step)
        if DP[current + next_step] == -1:
            DP[current + next_step] = DP[current] + 1
else:
    print(DP[-1])