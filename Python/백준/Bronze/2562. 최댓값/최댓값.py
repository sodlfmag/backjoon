import sys
arr = list(map(int, sys.stdin.read().splitlines()))
MAX = max(arr)
print(MAX, arr.index(MAX) + 1)