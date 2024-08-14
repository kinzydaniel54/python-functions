def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."


def main():
    print("Welcome to the basic calculator!")
    operation = input("Choose the operation (add, subtract, multiply, divide): ").lower()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    
    if operation == 'add':
        print(f"The result is: {add(num1, num2)}")
    elif operation == 'subtract':
        print(f"The result is: {subtract(num1, num2)}")
    elif operation == 'multiply':
        print(f"The result is: {multiply(num1, num2)}")
    elif operation == 'divide':
        result = divide(num1, num2)
        print(f"The result is: {result}" if isinstance(result, float) else result)
    else:
        print("Error: Invalid operation.")

if __name__ == "__main__":
    main()