def calculator():
    try:
        # Ask the user to input two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Ask for the operation
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform the operation
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator function
calculator()
