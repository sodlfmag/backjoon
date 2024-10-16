s = input()
arr = [-1] * 26
for i in range(26):
    idx = s.find(chr(ord('a') + i))
    arr[i] = idx

arr = list(map(str, arr))
result = ' '.join(arr)
print(result)