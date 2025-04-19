#code 5

original_string = "   Hello World!   "
left_stripped_string = original_string.lstrip()
print(left_stripped_string)  # Output: "Hello World!   "

custom_left_strip_string = "xxxyHello World!"
left_stripped_custom_string = custom_left_strip_string.lstrip("xy")
print(left_stripped_custom_string)  # Output: "Hello World!"

original_string = "   Hello World!   "
right_stripped_string = original_string.rstrip()
print(right_stripped_string)  # Output: "   Hello World!"

custom_right_strip_string = "Hello World!xxxy"
right_stripped_custom_string = custom_right_strip_string.rstrip("xy")
print(right_stripped_custom_string)  # Output: "Hello World!"

original_string = "Hello World! Welcome to Python."
split_string = original_string.split()
print(split_string)  # Output: ['Hello', 'World!', 'Welcome', 'to', 'Python.']

custom_split_string = "apple,banana,cherry"
split_custom_string = custom_split_string.split(",")
print(split_custom_string)  # Output: ['apple', 'banana', 'cherry']