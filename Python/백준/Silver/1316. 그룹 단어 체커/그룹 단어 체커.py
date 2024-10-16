import sys
n = int(input())
sample = list(sys.stdin.read().splitlines())
sample = [list(i)for i in sample]
seqdel = []
cnt = 0

# 반복 연속 삭제
for i in range(n):
    flag = sample[i][0]
    for j in range(1, len(sample[i])):
        if(sample[i][j] == flag):
            sample[i][j] = ''
        else:
            flag = sample[i][j]
    seqdel.append(''.join(sample[i]))

# 리스트화 -> SET화 후 길이 달라지면 그룹 X
s_list = [list(i)for i in seqdel]
set_list = [set(i)for i in s_list]

for i in range(n):
    if(len(s_list[i]) == len(set_list[i])):
        cnt += 1
print(cnt)