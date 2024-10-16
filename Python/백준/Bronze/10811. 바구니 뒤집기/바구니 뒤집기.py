import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(range(n+1))

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    temp = arr[a:b+1]
    temp.reverse()
    for j in range(a, b+1):
        arr[j] = temp[j-a]

result = ''
for i in range(1, n+1):
    result += str(arr[i]) + ' '

print(result[:-1])