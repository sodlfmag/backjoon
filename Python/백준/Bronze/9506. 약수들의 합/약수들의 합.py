import sys, math
inputs = []
result = []
while True:
    n = int(sys.stdin.readline().rstrip())
    if(n == -1):
        break
    inputs.append(n)

for i in range(len(inputs)):
    factors = []
    n = inputs[i]
    for j in range(1, n-1):
        if(n % j == 0):
            factors.append(j)

    if(sum(factors) == n):
        factors.sort()
        factors = list(map(str, factors))
        sums = ' + '.join(factors)
        print(f'{n} = {sums}')
    else:
        print(n, 'is NOT perfect.')