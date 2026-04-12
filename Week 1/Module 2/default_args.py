
# In normal function 
def sum(num):
    print(num)

sum(10) # in this function if i giver 2 perametter then the function doesn't work

# Now i given 2 peramitter in function
def sum2(num1,num2):
    result = num1 + num2
    print(result)

sum2(10,10) # in this function if i don't given 1 perametter or more then 2 perametter then the function doesn't work

# Now i will use a method that name is "star args" in this method we will give multiple perametter 
def arg(*numbers):
    print(numbers)

arg(10,20,30,40,50,60,70,80,90)