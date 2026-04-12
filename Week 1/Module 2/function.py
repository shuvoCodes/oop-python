
# To define a function in python then we write def
def double_it(num) :
    result = num * 2
    print(result) # hear don't have any return type data it's giver output directly

#Call the function
double_it(2)

#Now , We sum 2 number then we write
def sum(num1,num2):
    result_sum = num1 + num2
    return result_sum

def_sum = sum(10,20)
print("def_sum: ",def_sum)

#we can use print and return both in function
def double_it2(num) :
    result = num * 2
    print(result)
    return result

double_res = double_it2(def_sum)
print("doubel_res: ",double_res)