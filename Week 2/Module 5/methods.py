# A Method is a Function that is write in inside the class

class Phone:
    name ='Redmi'
    color = 'Black'
    price = 21000

    # inside the class if i use a function then i must a "self" perameter . if i don't include this it's don't work
    def call(self):
        print('You Missed a call.')

    def massage(self,phone,sms):
        return f'{sms} is from this number {phone}'
        

my_class = Phone()
res = my_class.call() # Output : You Missed a call.
sms = my_class.massage(901234,'I Love You')
print(sms) # output : I Love You is from this number 901234

