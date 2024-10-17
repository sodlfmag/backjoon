import sys
arr = [['']*15 for _ in range(5)]
for i in range(5):
    temp = list(sys.stdin.readline().rstrip())
    for j in range(len(temp)):
        arr[i][j] = temp[j]
result = ''
for j in range(15):
    for i in range(5):
        result += arr[i][j]
print(result)