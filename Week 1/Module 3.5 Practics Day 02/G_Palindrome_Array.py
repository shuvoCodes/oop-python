n = int(input())
arr = list(map(int,input().split()))
 
 
if arr[0:n] == arr[::-1]:
    print('YES')
    
else:
    print('NO')