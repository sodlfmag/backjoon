import sys
n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
length = len(cards)
maxv = 0
for i in range(length-2):
    for j in range(i+1, length-1):
        for k in range(j+1, length):
            sample = cards[i] + cards[j] +cards[k]
            if(sample > maxv and sample <= m):
                maxv = sample

print(maxv)