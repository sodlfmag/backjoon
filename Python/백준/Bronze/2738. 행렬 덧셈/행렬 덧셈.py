import sys
n, m = map(int, input().split())
matrix_A = []
matrix_B = []
for i in range(n):
    matrix_A.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    matrix_B.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        matrix_A[i][j] += matrix_B[i][j]

str_result = [map(str, i) for i in matrix_A]

for i in range(n):
    print(' '.join(str_result[i]))