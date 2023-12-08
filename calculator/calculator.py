def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def main():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        choice = int(input("Enter operation choice (1-4): "))
        if choice < 1 or choice > 4:
            print("Invalid choice. Please enter a number between 1 and 4.")
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                result = add(num1, num2)
                print("Result:", result)
            elif choice == 2:
                result = subtract(num1, num2)
                print("Result:", result)
            elif choice == 3:
                result = multiply(num1, num2)
                print("Result:", result)
            elif choice == 4:
                result = divide(num1, num2)
                print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter valid numbers for calculation.")

if __name__ == "__main__":
    main()