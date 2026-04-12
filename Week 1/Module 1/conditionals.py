# in, not, not in, is, is not 
# >, <, >=, <=, ==, !==
# and, or

a = 1
boss = False
if a > 5:
    print( 'Greater then 5')
elif a > 3:
    print('Little big')
elif a == 2:
    print('Equla')
else:
    print('Jinga la la hu hu')

# if boss is not True:
#     print('Boss is not to come in office')
# else: 
#     print('Boss in office')

if boss is not True:
    print('Boss in office')
else: 
    print('Boss is not to come in offic')

coin = 'head'
# nested conditions
if boss == True:
    print('great Boss')
    if coin == 'tail':
        print('batting')
    else:
        print('bowling')
        if 5 > 2 or boss != True:
            print('do  something')
            if 8%2 == 0 and 5%2==1:
                print('even 8 is an even number')
else:
    print('you are loss not a boss')