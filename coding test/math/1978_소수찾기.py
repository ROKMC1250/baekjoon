import sys
input = sys.stdin.readline
#############이렇게 하면 시간이 오히려 많이 걸린다.#################
# N = 1000
# prime = [True for i in range(N+1)]
# for i in range (2, int(N**(0.5)) + 1):
#     if prime[i]:
#         j = 2
#         while i * j <= N:
#             prime[i * j] = False
#             j += 1
# k = int(input())
# L = list(map(int, input().split()))
# result = 0
# for i in L:
#     if i == 1:
#         continue
#     elif prime[i]:
#         result += 1
# print(result)


N = int(input())
output = 0
num = list(map(int, input().split()))
for i in num:
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        output += 1
print(output)