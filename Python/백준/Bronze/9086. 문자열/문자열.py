import sys
n = int(input())
arr = list(sys.stdin.read().splitlines())
for i in range(len(arr)):
    print(arr[i][0] + arr[i][-1])