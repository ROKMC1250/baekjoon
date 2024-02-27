import sys
import math
input = sys.stdin.readline
A, B = map(int, input().rstrip().split())
##########math 라이브러리를 사용하여 구할수도 있다.###############
# print(math.gcd(A, B))
# print(math.lcm(A, B))
Z = (A * B)
while A % B != 0:
    A, B = B, A % B
print(B)
print(Z // B)
