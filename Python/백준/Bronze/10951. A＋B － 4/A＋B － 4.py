import sys
arr = list(sys.stdin.read().splitlines())

for i in range(len(arr)):
    a, b = map(int, arr[i].split())
    print(a+b)