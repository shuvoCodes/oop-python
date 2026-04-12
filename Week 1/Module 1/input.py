# To take input form user then we used 
# input()

take_money = input("give me money: ")
print("Here is your money: ", take_money)

take_from_father = input("Dad, give me some money: ")
print("from father: ",take_from_father)

total_money = take_money + take_from_father
print("Total money: ", total_money) 
# the output is of this code is 80100 but the output will be 180
# So. We see the input that will from user that data type is string. Now we convert string to integer data type

take_money_int = int(take_money)
take_from_father_int = int(take_from_father)

total_money_int = take_money_int + take_from_father_int
print("the int total money: ", total_money_int) # now the output is 180

# in other way 
print(int(take_money) + int(take_from_father))