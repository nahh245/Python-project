original_string = "hello world!"
capitalized_string = original_string.capitalize()
print(capitalized_string)  # Output: Hello world!

original_string = "Hello World!"
swapped_case_string = original_string.swapcase()
print(swapped_case_string)  # Output: hELLO wORLD!

original_string = "Hello World!"
index = original_string.find("World")
print(index)  # Output: 6

# Example of not finding a substring
not_found_index = original_string.find("Python")
print(not_found_index)  # Output: -1