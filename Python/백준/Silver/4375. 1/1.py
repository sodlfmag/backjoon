import sys

inputs = list(map(int, sys.stdin.read().splitlines()))

for i in range(len(inputs)):
    flag = True
    operand = '1'
    while(flag):
        if(int(operand) % inputs[i] == 0):
            flag = False
        else:
            operand += '1'
    print(len(operand))   
    