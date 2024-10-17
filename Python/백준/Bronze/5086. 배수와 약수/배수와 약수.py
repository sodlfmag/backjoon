import sys
inputs = []
while True:
    a, b = map(int, sys.stdin.readline().split())
    if(a == 0 and b == 0):
        break
    inputs.append([a,b])

for i in range(len(inputs)):
    a, b = inputs[i]
    # 약수
    if((b / a) % 1 == 0):
        print('factor')
    elif((a / b) % 1 == 0):
        print('multiple')
    else:
        print('neither')