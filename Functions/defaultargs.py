def addition(a, b=10):
    print(a, b)
    return a + b
# Input with validation for integer values
try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(addition(x))  # Calls the function with default value for b
    print(addition(x, y))  # Calls the function with provided value for b
except ValueError:
    print("Please enter valid integers.")

