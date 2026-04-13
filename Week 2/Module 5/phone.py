# make a class
class Myclass:
    pass # its mean i pass the class. I don't write any more in this class

class Phone:
    name = 'Redmi'
    Color = 'Black'
    price = 21000

# call the class
My_class = Phone()

# print just My_class
print(My_class) # Output: <__main__.Phone object at 0x000002004D5886E0> 

# print Phone object
print(My_class.name) # Output : Redmi
print(My_class.Color) # output : Black
print(My_class.price) # Output : 21000
