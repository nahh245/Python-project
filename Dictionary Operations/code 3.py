# creating python dictionary

# 7. setdefault
my_dict = {'a': 1, 'b': 2}

# If 'c' is not present, add it with value 3
value = my_dict.setdefault('c', 3)
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
print(value)    # Output: 3

# 8. clear

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
print(my_dict)  # Output: {}

# 9. fromkeys

keys = ['a', 'b', 'c']
value = 0
new_dict = dict.fromkeys(keys, value)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}
