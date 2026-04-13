class Shop:
    cart = []   # class attribute

    def __init__(self,buyer):
        self.buyer = buyer

    def add_to_cart(self,item):
        self.cart.append(item)

customer1 = Shop('Shuvo')
customer1.add_to_cart('Show')
customer1.add_to_cart('pent')
print(customer1.cart) # Output : ['Show', 'pent']

customer2 = Shop('Sumu')
customer2.add_to_cart('Lipstic')
customer2.add_to_cart('High Hill')
print(customer2.cart) # Output : ['Show', 'pent', 'Lipstic', 'High Hill']

# Here is the problem When i include customer 2 product then my Output showed Customer1 and customer2 products
# Because i declear class attribute then all the input store in cart 