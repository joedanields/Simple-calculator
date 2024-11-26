# Defining all the operation functions
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed."

# Main calculator function
def calculator():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Getting user's choice
    try:
        choice = int(input("Enter the choice (1, 2, 3, or 4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please select a valid option.")
            return

        # Getting input numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Performing the selected operation
        if choice == 1:
            print(f"Result: {addition(num1, num2)}")
        elif choice == 2:
            print(f"Result: {subtraction(num1, num2)}")
        elif choice == 3:
            print(f"Result: {multiplication(num1, num2)}")
        elif choice == 4:
            print(f"Result: {division(num1, num2)}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Using a loop to calculate multiple times
while True:
    option = input("Do you want to start or continue? Enter 'yes' to proceed or 'no' to quit: ").strip().lower()
    if option == "yes":
        calculator()
    elif option == "no":
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
