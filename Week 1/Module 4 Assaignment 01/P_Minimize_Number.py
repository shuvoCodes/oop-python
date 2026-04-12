n = int(input())
arr = list(map(int,input().split()))
cnt = 0
br = True
while True:
    if not br:
        break
    for i in range(n):
        if arr[i] % 2 != 0:
            br = False
            break
            
        else:
            arr[i] = arr[i] / 2
    if br:
        cnt += 1

print(cnt)