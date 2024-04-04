import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
DP = [[0] * (M+1)] * (N+1)
miro = []
for _ in range(N):
    miro.append(list(map(int,input().rstrip().split())))
for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = max(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + miro[i-1][j-1]
print(DP[N][M])