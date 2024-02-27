import sys
input = sys.stdin.readline
while True:
    try:
        num = int(input().rstrip())
    except:
        break
    i = '1'
    while int(i) % num != 0:
        i += '1'
    print(len(i))