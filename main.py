def add(a,b):
    return a+b

def subtract(a,b):
    return a-b 

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a/b

try:
    print("FUNCTION CALCULATOR")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (add, subtract, multiply, divide): ")

    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)
    else:
        raise ValueError("Invalid operation.")

    print(f"Result: {result}")

    print("Thank you for using the calculator.")

except ValueError:
    print("Error: cannot divide by zero.")
