cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
cnt = 0
total = len(s)

for i in range(len(cro)):
    if(cro[i] in s):
        temp = s.count(cro[i])
        cnt += temp
        total -= len(cro[i]) * temp

if('dz=' in s):
    total += (s.count('dz='))

print(cnt + total)