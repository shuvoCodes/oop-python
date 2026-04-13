# Homework 01

class calculator:
    brand = 'Casio Ms 100'

    def add( self, num1,num2):
        print(num1 + num2)

    def negative(self, num1,num2):
        print(num1 - num2)

    def multi(self,num1,num2):
        print(num1 * num2)

    def divi(self, num1,num2):
        print(num1 / num2)
    
calulat = calculator()

calulat.add(10,20)  # Output: 30
calulat.negative(5,1)    # Output: 4  
calulat.multi(5,2)    # Output: 10
calulat.divi(20,2)   # Output: 10.0
print(calculator().brand) # Output : Casio Ms 100
