"""
    1 -> when declar a variable in class that called class Attribute
    2 -> When declar a variable in constructur that called Instance Attribute
"""

class shop:

    def __init__(self,owner):
        self.owner = owner
        self.cart = [] # Instance Attribute

    def add_to_cart(self,item):
        self.cart.append(item)

customer1 = shop('Shuvo')
customer1.add_to_cart('Show')
customer1.add_to_cart('watch')
print(customer1.cart) # Output : ['Show', 'watch']

customer2 = shop('Sumu')
customer2.add_to_cart('Lipstic')
customer2.add_to_cart('Dress')
print(customer2.cart) # Output : ['Lipstic', 'Dress']
        