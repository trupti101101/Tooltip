def add(x, y):
    # Attempt to add as numbers first, if it fails, concatenate as strings
    try:
        return float(x) + float(y)
    except ValueError:
        return str(x) + str(y)

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("==| Welcome To Math Calculator |==")
    print("Select operation:")
    print("1. Addition (Numeric or String)")
    print("2. Subtraction (Numeric)")
    print("3. Multiplication (Numeric)")
    print("4. Division (Numeric)")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = input("Enter first operand: ")
            num2 = input("Enter second operand: ")

            try:
                if choice != '1':
                    num1 = float(num1)
                    num2 = float(num2)

            except ValueError:
                print("Invalid input. Please enter numeric values for numeric operations.")
                continue

            if choice == '1':
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                if isinstance(num1, float) and isinstance(num2, float):
                    result = subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                else:
                    print(f"Invalid operands for numeric subtraction.")
            elif choice == '3':
                if isinstance(num1, float) and isinstance(num2, float):
                    result = multiply(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                else:
                    print(f"Invalid operands for numeric multiplication.")
            elif choice == '4':
                if isinstance(num1, float) and isinstance(num2, float):
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")
                else:
                    print(f"Invalid operands for numeric division.")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                print("Exiting the math calculator.")
                break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    calculator()
