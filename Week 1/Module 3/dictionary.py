List_num = [1, 2, 3, 12, 4, 1, 2, 12, 3]
person1 = ['Sumu','PM er More', 25,'Bad Student']
print(person1) # OutPut : ['Sumu', 'PM er More', 25, 'Bad Student']

# Key value pair
# dictionary 
# Object
# Hash Tabel 
# Overlap With Set
# Struture of Dectionary : {key: value, key: value, key: value}

person = {'Name' : 'Nusu', 'Address' : 'Narayanganj', 'age' : 25, 'Job' : 'Student'} # dictionary 
print(person) #Outout : {'Name': 'Nusu', 'Address': 'Narayanganj', 'age': 25, 'Job ': 'Student'}
print(person['Name']) #outPut: Nusu
print(person['Address']) # Output: Narayanganj
print(person['age']) # Output : 25
print(person['Job']) # Output : Student
print(type(person))  #Output : <class 'dict'>

# To see the dictionary keys then uset keys() function
print(person.keys()) # Output : dict_keys(['Name', 'Address', 'age', 'Job'])
# To see the dictionary value then uset values() function
print(person.values()) # Output : dict_values(['Nusu', 'Narayanganj', 25, 'Student'])

# To add a new key and value then
person['Language'] = 'python'
print(person) # Output : {'Name': 'Nusu', 'Address': 'Narayanganj', 'age': 25, 'Job': 'Student', 'Language': 'python'}
#change the tital value
person['Name'] = 'Jahan'
print(person) # Output : {'Name': 'Jahan', 'Address': 'Narayanganj', 'age': 25, 'Job': 'Student', 'Language': 'python'}

#To delete a title and value
del person['Job']
print(person) # Output : {'Name': 'Jahan', 'Address': 'Narayanganj', 'age': 25, 'Language': 'python'}

#spacial dictionary Looping 
for key, value in person.items():
    print(key, ' -> ', value) 
#output: 
# Name  ->  Jahan
# Address  ->  Narayanganj
# age  ->  25
# Language  ->  python
