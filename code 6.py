#code 6

words = ["Hello", "World", "from", "Python"]
joined_string = " ".join(words)
print(joined_string)  # Output: "Hello World from Python"

# Using a different separator
csv_string = ",".join(["apple", "banana", "cherry"])
print(csv_string)  # Output: "apple,banana,cherry"

alphabetic_string = "HelloWorld"
print(alphabetic_string.isalpha())  # Output: True

mixed_string = "Hello123"
print(mixed_string.isalpha())  # Output: False

empty_string = ""
print(empty_string.isalpha())  # Output: False

digit_string = "12345"
print(digit_string.isdigit())  # Output: True

mixed_string = "123abc"
print(mixed_string.isdigit())  # Output: False

# Check with a string containing white spaces
whitespace_string = " 123 "
print(whitespace_string.isdigit())  # Output: False