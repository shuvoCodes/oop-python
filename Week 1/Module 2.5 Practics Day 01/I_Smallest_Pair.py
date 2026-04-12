t = int(input())
for k in range(t):
    n = int(input())
    arr =list(map(int,input().split()))
    if n < 2:
        print(0)
        continue
    ans = float('inf')
    for i in range(n+1):
        for j in range(i+1,n):
            res = (arr[i]+arr[j]) + (j - i)
            ans = min(res,ans)

    print(ans)
    