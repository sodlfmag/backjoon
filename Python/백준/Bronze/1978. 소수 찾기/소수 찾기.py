import sys, math
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(n):
    temp = arr[i]
    flag = True
    if(temp == 1):
        continue

    for j in range(2, int(math.sqrt(temp))+1):
        if(temp % j == 0):
            flag = False
            break
    
    if(flag):
        cnt += 1

print(cnt)