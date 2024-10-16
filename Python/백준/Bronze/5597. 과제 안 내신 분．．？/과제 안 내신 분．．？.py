import sys
total = set(range(1, 31))
at = set(map(int, sys.stdin.read().splitlines()))

result = list(total - at)
result.sort()
print(result[0])
print(result[1])