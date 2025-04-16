#code 3


original_string = "Hello World!"
index = original_string.index("World")
print(index)  # Output: 6

# Example of not finding a substring
try:
    not_found_index = original_string.index("Python")
except ValueError as e:
    print(e)  # Output: substring not found


original_string = "Hello World!"
starts_with_hello = original_string.startswith("Hello")
print(starts_with_hello)  # Output: True

starts_with_python = original_string.startswith("Python")
print(starts_with_python)  # Output: False


original_string = "Hello World!"
ends_with_world = original_string.endswith("World!")
print(ends_with_world)  # Output: True

ends_with_python = original_string.endswith("Python")
print(ends_with_python)  # Output: False