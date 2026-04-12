n = int(input())

fib = [0,1]

for i in range(n-2):
    fib.append(fib[i] + fib[i+1])

x = fib[n-1]
print(x)
