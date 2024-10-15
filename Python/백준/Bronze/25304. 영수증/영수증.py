import sys
total = int(input())
N = int(input())

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    total -= a * b

if(total == 0):
    print('Yes')
else:
    print('No')