import sys
input = sys.stdin.readline


N = 1000000
prime = [True for i in range(N + 1)]
for i in range(3, int(N**(0.5))+1, 2): 
    if prime[i] == True: 
        j = 2
        while i * j <= N:
            prime[i * j] = False
            j += 1

while True:
    num = int(input())
    if num == 0:
        break
    for i in range(3, num + 1, 2):
        if prime[i] and prime[num-i]:
            print(f"{num} = {i} + {num-i}")
            break
        elif i == num:
            print("Goldbach's conjecture is wrong")
            
