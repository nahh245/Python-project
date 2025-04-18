#code 4


original_string = "Hello Ethiopia! Welcome to the Ethiopia!"
count_world = original_string.count("Ethiopia")
print(count_world)  # Output: 2

count_l = original_string.count("l")  # Count occurrences of 'l'
print(count_l)  # Output: 3


original_string = "Hello World! Welcome to the World!"
replaced_string = original_string.replace("World", "Python")
print(replaced_string)  # Output: Hello Python! Welcome to the Python!

replaced_string_limited = original_string.replace("World", "Python", 1)
print(replaced_string_limited)  # Output: Hello Python! Welcome to the World!


original_string = "   Hello World!   "
stripped_string = original_string.strip()
print(stripped_string)  # Output: "Hello World!"

custom_strip_string = "xxxyHello World!yyyst"
stripped_custom_string = custom_strip_string.strip("xy")
print(stripped_custom_string)  # Output: "Hello World!"