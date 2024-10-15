N, X = map(int, input().split())
arr = list(map(int, input().split()))
result = []
result_str = ''
for i in range(N):
    if(arr[i] < X):
        result.append(arr[i])

for i in range(len(result)):
    result_str += str(result[i]) + ' '

print(result_str[:-1])