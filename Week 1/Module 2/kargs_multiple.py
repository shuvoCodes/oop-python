# make kars
def fullName(first,last):
    name = f'My Name is {first} {last}'
    return name

name = fullName('Shakhawat','Hossain')
print(name)

# don't use pererameter in order(serialy)
def gf_name(first,last):
    name = f'My girlfriend name is {first} {last}'
    return name

gf_name_is = gf_name(last= 'Jahan',first='Nusrat')
print(gf_name_is)

# def famous(**kargs)
def _famous(fast,last,**additional):
    print(fast,last,additional)
    # print(additional['tital'])
    for tit,val in additional.items():
        print(tit,val)

_famous(fast="ABC",last="abc",tital="DEF",title="def")

# return multiple things from an array
def a_lot(num1, num2):
    sum = num1 + num2
    mult = num1 * num2
    remain = num1 - num2
    # return [sum, mult, remain]
    return sum, mult, remain


everything = a_lot(55, 21)
print(everything)
