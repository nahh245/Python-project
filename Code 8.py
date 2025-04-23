#code 8

name = "Nahom"
age = 20
greeting = f"My name is {name} and I am {age} years old."
print(greeting)  # Output: "My name is Nahom and I am 20 years old."

# You can also perform expressions inside the braces
a = 5
b = 10
result = f"The sum of {a} and {b} is {a + b}."
print(result)  # Output: "The sum of 5 and 10 is 15."

my_string = "Hello, World!"
length = len(my_string)
print(length)  # Output: 13

my_list = [1, 2, 3, 4, 5]
list_length = len(my_list)
print(list_length)  # Output: 5

original_string = "Hello, World!"
encoded_string = original_string.encode('utf-8')
print(encoded_string)  # Output: b'Hello, World!'

# Encoding with errors handling
non_ascii_string = "Café"
ascii_encoded = non_ascii_string.encode('ascii', 'ignore')
print(ascii_encoded)  # Output: b'Caf'