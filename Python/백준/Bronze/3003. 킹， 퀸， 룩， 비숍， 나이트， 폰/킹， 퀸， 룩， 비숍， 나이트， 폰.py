std = [1, 1, 2, 2, 2, 8]
result = [0] * 6
arr = list(map(int,input().split()))

for i in range(len(result)):
    result[i] = std[i] - arr[i]

result = list(map(str, result))
print(' '.join(result))