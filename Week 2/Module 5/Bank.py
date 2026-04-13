
class Bank:

    def __init__(self,balance):
        self.balance = balance
        self.min_withdaws = 100
        self.max_withdaws = 100000
    
    def get_balance(self):
        print( self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self,amount):
        if amount < 100:
            print(f'You can\'t withdraw less then {self.min_withdaws}')
        elif amount > 100000:
            print(f'you can\'n whithdaw more then {self.max_withdaws}')
        else:
            self.balance -= amount
            print(f'Here is your cash : {amount}')

brac = Bank(5000)
brac.get_balance() # Output: 5000
brac.deposit(1000)
brac.get_balance() # Output: 6000
brac.withdraw(50)  # Output: You can't withdraw less then 100
brac.withdraw(500) # Output: Here is your cash : 500
brac.get_balance() # Output: 5500
brac.deposit(2000)
brac.get_balance() # Output: 7500
brac.withdraw(200000) # Output: you can'n whithdaw more then 100000