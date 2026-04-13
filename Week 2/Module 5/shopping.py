class shopping:

    def __init__(self,name):
        self.name = name
        self.cart = []
    
    # Add a product in Cart
    def add_to_cart(self,item,price,quantity):
        product = {'item': item,'price':price,'quantity':quantity}
        self.cart.append(product)

    # Chackout 
    def chakout(self,amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
            
        if amount < total:
            print(f'Give me more {total - amount} Taka')
        elif amount > total:
            print(f'Wait, I will give back {amount - total} Taka')
        else: 
            print(f'Thank You Purchase. Your product price is {total} Taka.')

cus1 = shopping('Shuvo')
cus1.add_to_cart('Phone Cover',100,20)
cus1.add_to_cart('Garila Glass',50,60)
cus1.add_to_cart('EarePhone',70,80)

print(cus1.cart)  # Output: [{'item': 'Phone Cover', 'price': 100, 'quantity': 20},
                            #{'item': 'Garila Glass', 'price': 50, 'quantity': 60},
                            #{'item': 'EarePhone', 'price': 70, 'quantity': 80}]

cus1.chakout(100)   #Output : Give me more 10500 Taka
cus1.chakout(10600) # Output : Thank You Purchase. Your product price is 10600 Taka.
cus1.chakout(20000) #Output : Wait, I will give back 9400 Taka