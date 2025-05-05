# 1. values

users: dict = {0: 'michel', 1: 'denzel', 2: 'tom'}
print(users.values())  # To print all values


# 2. keys

users: dict = {0: 'morgan', 1: 'brad', 2: 'leonardo'}
print(users.keys())   # To print all keys


# 3. pop

users: dict = {0: 'jack', 1: 'matt', 2: 'kate'}
print(users.pop(2))   # Remove and return the item with key 2
print(users)          # Print the remaining dictionary