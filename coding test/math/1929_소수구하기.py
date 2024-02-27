import sys
input = sys.stdin.readline
N = 1000000
prime = [True for i in range(N+1)]
for i in range(2, int(N**(0.5)) + 1):
    if prime[i]:
        j = 2
        while i * j <= N:
            prime[i * j] = False
            j += 1
min, max = map(int, input().split())
for i in range(min, max + 1):
    if i == 1:
        continue
    elif prime[i]:
        print(i)


