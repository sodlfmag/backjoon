import sys
n, m = map(int, input().split())
basket = [0] * (n+1)
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    for j in range(a, b+1):
        basket[j] = c

result = ''
for i in range(1, n+1):
    result += str(basket[i]) + ' '

print(result[:-1])