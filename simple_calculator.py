# Display operation choices
print("Choose an operation:")

# Define available operations
operations = ('''sum = 1
product = 2
divide = 3
subtract = 4
power = 5
remainder = 6''')

# Show the list of operations
print(operations)

# Take first number input from the user
a = int(input("First number: "))

# Take second number input from the user
b = int(input("Second number: "))

# Take the operation choice input from the user
x = int(input("Enter the number corresponding to the operation (1 to 6): "))

# Define the calculator function
def calc():
    if x == 1:
        # Sum
        print('Result:', a + b)
    elif x == 2:
        # Product
        print('Result:', a * b)
    elif x == 3:
        # Division with zero check
        if b == 0:
            print("Cannot divide by zero")
        else:
            print('Result:', a / b)
    elif x == 4:
        # Subtraction
        print('Result:', a - b)
    elif x == 5:
        # Exponentiation (a to the power of b)
        print('Result:', a ** b)
    elif x == 6:
        # Remainder
        print('Result:', a % b)
    else:
        # Invalid operation
        print("Invalid operation")

# Call the calculator function
calc()
