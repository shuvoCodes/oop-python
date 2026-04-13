# Homeword 02

class pen:
    
    def __init__(self, brand, color, price):
        self.name = brand
        self.color = color
        self.price = price

pen_pri = pen('Metador', 'Black', 5)
print(pen_pri.name,pen_pri.color,pen_pri.price) # output : Metador Black 5