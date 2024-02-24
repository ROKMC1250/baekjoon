import sys
from collections import deque
input = sys.stdin.readline

input = input().rstrip().split()
num = int(input[0])
div = int(input[1])

stack = [i for i in range(1,num+1)]
result = []
delete = []

        
        
