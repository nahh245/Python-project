# creating dictionary

 # 4. popitem()
users: dict = {0: 'J.cole', 1: 'Teddy', 2: 'future'}
print("Before popitem:", users)
users.popitem()
print(users)

# 5. copy()
sample_dict: dict = {0: ['a', 'b'], 1: ['c', 'd']}
my_copy: dict = sample_dict.copy()
print(sample_dict)
print(my_copy)

# 6. get()
users: dict = {0: 'mario', 1: 'james', 2: 'cole'}
print(users.get(1))

