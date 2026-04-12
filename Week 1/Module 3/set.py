# A set is a data type that is store a unique value. That means it don't store duplicate value 
# A set will define in " {} ". insite the {} every value will separet in " , "

first_set = {10,20,10,1,2,1,3,2}
# make a list
List_num = [1, 2, 3, 12, 4, 1, 2, 12, 3]

# print(first_set) #output : {1, 2, 3, 20, 10}
print(List_num) # output: [1, 2, 3, 12, 4, 1, 2, 12, 3]

# make set from list
make_set = set(List_num)
print(make_set) # Output : {1, 2, 3, 4, 12} remove the dublicate value

# Add the value in set
make_set.add(22)
print(make_set) # Output : {1, 2, 3, 4, 12, 22} Add the value 22 

# Remove the value from set
make_set.remove(4)
print(make_set) # Output : {1, 2, 3, 12, 22} remove the value 4

#don't use as a indexing
#print(make_set[1]) 
# make_set[1] = 1  >> don't change a value in set

# print value using for loop
for item in make_set:
    print('item',item)

# Find a value in set
if 2 in make_set:
    print('Found') # When 2 is same in make_set values Output is Found
else:
    print('Not Found') # when 2 is not same in make_set values then Output is Not Found

A = {1,2,3}
B = {2,4,5}

# Intersection Set
print(A & B) # output : {2}
# Union Set
print(A | B) # Output : {1, 2, 3, 4, 5}