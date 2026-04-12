num = input()
rev = int(str(num)[::-1])
print(rev)
if int(num) == rev:
    print("YES")
else:
    print("NO")