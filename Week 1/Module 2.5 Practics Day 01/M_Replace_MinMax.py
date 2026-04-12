n = input()
arr = list(map(int ,input().split()))

maximum = max(arr[::])
minimum = min(arr[::])
res = list()
for i in arr:
    if i == maximum:
        res.append(minimum)
    elif i == minimum:
        res.append(maximum)
    else:
        res.append(i)

for i in res:
    print(i,end=' ')