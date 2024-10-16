import sys
n = int(input())
for i in range(n):
    cnt, s = map(str, sys.stdin.readline().split())
    cnt = int(cnt)
    temp = ''
    for j in range(len(s)):
        temp += s[j] * cnt
    print(temp)