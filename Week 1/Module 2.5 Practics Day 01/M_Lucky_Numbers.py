a ,b = map(int,input().split())

found = False

for i in range(a,b+1):
    lucky = True
    for num in str(i):
        if num != '4' and num != '7':
            lucky = False
            break
    if lucky:
        found = True
        print(i,end = ' ')
if not found:
    print(-1)