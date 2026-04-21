# 2. Inside the Shop class, 
# create a method name add_product 
# which adds products using the Product class to the Shop class.

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
class Shop:
    def __init__(self):
        self.product_list = []

    def add_product(self,product):
        self.product_list.append(product)
    
    def show_product(self):
        for item in self.product_list:
            print( f'Name: {item.name}, Price: {item.price}, Quantity: {item.quantity}')

products = Product('Glass',100,1)
products2 = Product('Pen',15,5)

product_list = Shop()

product_list.add_product(products)
product_list.add_product(products2)
product_list.show_product()

# Output:
#Name: Glass, Price: 100, Quantity: 1
#Name: Pen, Price: 15, Quantity: 5