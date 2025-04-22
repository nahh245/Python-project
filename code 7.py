#code 7

alphanumeric_string = "Hello123"
print(alphanumeric_string.isalnum())  # Output: True

string_with_space = "Hello 123"
print(string_with_space.isalnum())  # Output: False

empty_string = ""
print(empty_string.isalnum())  # Output: False

whitespace_string = "   "
print(whitespace_string.isspace())  # Output: True

mixed_string = "Hello World"
print(mixed_string.isspace())  # Output: False

empty_string = ""
print(empty_string.isspace())  # Output: False

name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: "My name is Alice and I am 30 years old."

# Using numbered placeholders
formatted_numbered = "The {1} is a {0}.".format("cat", "animal")
print(formatted_numbered)  # Output: "The animal is a cat."

# Using keyword arguments
formatted_keyword = "Hello {name}, welcome to {place}!".format(name="Bob", place="Python")
print(formatted_keyword)  # Output: "Hello Bob, welcome to Python!"