import sys
n = int(input()) 
points = []
contained = [[0]*100 for _ in range(100)]
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    points.append(temp)

for i in range(n):
    x, y = points[i]
    for j in range(x, x+10):
        for k in range(y, y+10):
            contained[j][k] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        cnt += contained[i][j]

print(cnt)