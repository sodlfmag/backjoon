import sys
n, m = map(int, input().split())
arr = [0] * (n+1)
for i in range(n+1):
    arr[i] = i

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

result = ''
for i in range(1, n+1):
    result += str(arr[i]) + ' '

print(result[:-1])