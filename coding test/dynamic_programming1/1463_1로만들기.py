import sys
input = sys.stdin.readline

N = int(input())
D = [[0] for _ in range(1000001)]
D[0].append(N)
if N == 1:
    print(0)
for i in range(1, N + 1):
    # print('-----------------------')
    # print('i:', i)
    # print('-----------------------')
    for j in range(1, len(D[i-1])):
        # print('j:', j)
        if D[i-1][j] % 3 == 0:
            D[i].append(D[i-1][j] // 3)
            if D[i-1][j] // 3 == 1:
                print(i)
                break
        if D[i-1][j] % 2 == 0:
            D[i].append(D[i-1][j] // 2)
            if D[i-1][j] // 2 == 1:
                print(i)
                break
        D[i].append(D[i-1][j] - 1)
        if D[i-1][j] - 1 == 1:
            print(i)
            break
        # print(D)
    else:
        continue
    break 
