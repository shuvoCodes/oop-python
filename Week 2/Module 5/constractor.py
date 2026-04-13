class Phone:
    manufaceded = 'China'

    # to make a constructor we must inistialize the __init__. If i don't use then it not work
    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

my_phn = Phone('Shuvo','Redmi',20000) # Phone class automatic detect the constractor
print(my_phn.owner,my_phn.brand,my_phn.price) #Output : Shuvo Redmi 20000
         
her_phn = Phone('Sumu', 'Poco', 15000)
print(her_phn.owner,her_phn.brand,her_phn.price) #Output : Sumu Poco 15000