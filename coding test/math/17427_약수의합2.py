import sys
input = sys.stdin.readline
N = int(input())
sum = 0
#######이렇게 하면 시간복잡도가 O(n * sqrt(n))이 된다.
# for i in range(1,N+1):
#     for j in range(1, int(i**(1/2))+1):
#         if i % j == 0:
#             if j == i//j:
#                 sum += j
#             else:
#                 sum += j
#                 sum += i // j
for i in range(1, N + 1):
    sum += i * (N // i)
print(sum)