# tuple is a data type that is store multiple value with onece
# tuple will define in "()"

def multi():
    return 3,4
print(multi())

thinks = 'Phone stand', 'Monitor','Controllar', 'Glass', 'Phone'
print(thinks) #output tuple
print(thinks[1]) # print index 1
print(thinks[1:4]) # print index 1 to 4
print(thinks[::-1]) # print in revers 

# Find a element in thinks
if 'Stapler' in thinks:
    print('Find')
else:
    print('Not Find')
