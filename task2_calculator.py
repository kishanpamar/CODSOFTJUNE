# Task 2 - Simple Calculator

print("Simple Calculator")

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operator.")
except ValueError:
    print("Please enter valid numbers.")
