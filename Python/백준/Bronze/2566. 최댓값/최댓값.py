import sys
max_v = -1
mat = sys.stdin.read().splitlines()
mat = [list(map(int, i.split())) for i in mat]
a = 0
b = 0
for i in range(9):
    for j in range(9):
        if(mat[i][j] > max_v):
            max_v = mat[i][j]
            a = i
            b = j

print(max_v)
print(a+1, b+1)