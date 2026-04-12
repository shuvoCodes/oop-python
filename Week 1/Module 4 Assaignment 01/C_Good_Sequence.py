from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

cnt = Counter(arr)
remove = 0
for x,c in cnt.items():
    if c < x:
        remove += c
    elif c > x:
        remove += c - x

print(remove)