h, m = map(int, input().split())
time = int(input())

time_h = time // 60
time_m = time % 60

h += time_h
m += time_m

if(m >= 60):
    h += 1
    m -= 60
if(h >= 24):
    h -= 24

print(h, m)
