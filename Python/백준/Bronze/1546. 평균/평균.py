n = int(input())
arr = list(map(int, input().split()))
MAX = max(arr)

result = []
for i in range(n):
    result.append((arr[i] / MAX) * 100)

print(sum(result) / n)