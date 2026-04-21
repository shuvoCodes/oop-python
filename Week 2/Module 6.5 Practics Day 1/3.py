# 3. Inside the Shop class,
# create a method name buy_product which is used to buy a product
# and check whether this product is available or not. 
# If you successfully buy a product, then throw a Congress message.

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
    
    def buy_product(self,product,quantity):
        self.flg = False
        for item in self.product_list:
            if item.name == product:
                if item.quantity >= quantity:
                    self.cash = item.price * quantity
                    print(f'Congractulations, You are successlly purchase {product} in {quantity} {self.cash}')
                    item.quantity -= quantity
                    self.flg = True
                    break
        if not self.flg:
            print('Sorry, We don\'n have this product')

            
p1 = Product('Glass', 100,100)
p2 = Product('Phone',20000,10)
shop = Shop()

shop.add_product(p1)
shop.add_product(p2)

shop.buy_product('Glass',1)
shop.buy_product('Phone',2)
shop.buy_product('Pen',2)