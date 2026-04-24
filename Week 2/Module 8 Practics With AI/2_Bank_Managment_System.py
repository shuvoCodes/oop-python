# Bank Managment System

class BankDatabase:
    account_list = []

    @classmethod
    def add_accoutn(cls,account):
        cls.account_list.append(account)

    @classmethod
    def view_account(cls):
        for acc in cls.account_list:
            view = Account.account_info(acc)
            print(view)

    
class Account:
    def __init__(self, account_number,name,balance,is_active = True):
        self.__account_number = account_number
        self.__name = name
        self.__balance = balance
        self.__is_active = is_active

        BankDatabase.add_accoutn(self)

    @classmethod
    def account_info(cls, acc):
        return f'Accout No: {acc.__account_number}, Name: {acc.__name}, Balance: {acc.__balance}, Active: {acc.__is_active}'
    
    @classmethod
    def deposit(self,account_num,amount):
        for acc in BankDatabase.account_list:
            if acc.__account_number == account_num:
                if not acc.__is_active :

                    print('Your Account is Deactiveted.\nDo You want to active Your account.\n1.Yes\n2.No')
                    inp = int(input('Enter Your chooes: '))
                    if inp == 1:
                        acc.__is_active = True
                        acc.__balance += amount 
                        print('Deposit Successful.')
                    elif inp == 2:
                        print('Account Deactivated')
                    else:
                        raise ValueError('Invalid Input')
                else:
                    acc.__balance += amount
                    print('You are successfully deposit')
                return
    @classmethod
    def withdraw(self,account_num,amount):
        for acc in BankDatabase.account_list:
            if acc.__account_number == account_num:
                if amount < 500 or amount > 10000:
                    raise ValueError('Not Withdraw this amount')
                elif amount < acc.__balance or amount < acc.__balance:
                    raise ValueError('Inceficint amount.')
                else:
                    acc.__balance -= amount
                    print('Here is Your amount')
            
        print('Not Found')
    @classmethod
    def deactivate_account(self,account_num):
        for acc in BankDatabase.account_list:
            if acc.__account_number == account_num:
                acc.__is_active = False
                print('Account Deactiveted Successfully')
                return
         

Account(10232, 'gpt', 200000, True)
Account(10233, 'shuvo', 15000, True)
Account(10234, 'rahim', 5000, False)
# Main Manu

while True:

    print('\n----------Account Management System----------\n')
    print('1. View Account')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Deactivate')
    print('5. Exit')

    try:
        x = int(input('Enter Your Choossen number: '))
        if x == 1:
            BankDatabase.view_account()
        if x == 2:
            acc_num = int(input('Enter Your account Number: '))
            amount = int(input('Enter Your Amount: '))
            Account.deposit(acc_num,amount)
        elif x == 3:
            acc_num = int(input('Enter Your account Number: '))
            amount = int(input('Enter Your Amount: '))
            Account.withdraw(acc_num,amount)
        elif x == 4:
            acc_num = int(input('Enter Your account Number: '))
            Account.deactivate_account(acc_num)
        elif  x == 5:
            break
        
    except ValueError as ve:
        print(ve)
    