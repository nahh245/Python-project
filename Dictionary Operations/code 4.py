fruits = {1: 'apple', 2: 'banana', 3: 'cherry'}
for key, value in fruits.items():
    print(f'key: {key}, value: {value}')
    
    
person = {'name' : 'alice' , 'age' : 25 }
person.update({'age' : 27, 'city': 'New York'})
print(person)