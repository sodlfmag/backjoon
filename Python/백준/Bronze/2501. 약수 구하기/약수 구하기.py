import sys
n, k = map(int, sys.stdin.readline().split())
factors = []

for i in range(1, n+1):
    if((n / i) % 1 == 0):
        factors.append(i)

if(len(factors) < k):
    print(0)
else:
    print(factors[k-1])