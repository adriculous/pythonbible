# Ask user for name (use "input" built-in function - check Python docs!)

name = input("What is your name?: ")
print(name)

# Ask user for age

age = input("How old are you?: ")

# Ask user for city

city = input("What city do you live in?: ")

# Ask user what they enjoy (doing)

love = input("What do you love doing?: ")

# Create output text (string concatenation: use "format" built-in function
# - check Python docs!). Use {} to represent the variables (placeholders)

string = "Your name is {} and you are {} years old. You live in {} and you love {}."
output = string.format(name, age, city, love)

# Print output to screen
print(output)
