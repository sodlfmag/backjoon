s = input().upper()
di = dict()
for i in range(len(s)):
    if(s[i] in di):
        di[s[i]] += 1
    else:
        di[s[i]] = 1

arr = [k for k,v in di.items() if max(di.values()) == v]
if(len(arr) == 1):
    print(arr[0])
else:
    print('?')