import sys


def addition(addition1, addition2):
    return addition1 + addition2


def subtraction(subtraction1, subtraction2):
    return subtraction1 - subtraction2


def multiplication(multiplication1, multiplication2):
    return multiplication1 * multiplication2


def division(division1, division2):
    if division2 == 0:
        return "Division by zero error!"
    return division1 / division2


while True:
    print(
        'Select the operation you want to perform:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division'
        '\n5. Exit')

    choice = input("Your choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting. Have a nice day!")
        sys.exit()

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice! Please select a valid option.")
        continue

    number1 = input("Enter the first number: ")
    if number1 == 'q':
        print("Exiting. Have a nice day!")
        sys.exit()

    number2 = input("Enter the second number: ")
    if number2 == 'q':
        print("Exiting. Have a nice day!")
        sys.exit()

    try:
        number1 = float(number1)
        number2 = float(number2)
    except ValueError:
        print("Invalid number input! Please enter a valid number.")
        continue

    if choice == '1':
        print("Result: ", addition(number1, number2))
    elif choice == '2':
        print("Result: ", subtraction(number1, number2))
    elif choice == '3':
        print("Result: ", multiplication(number1, number2))
    elif choice == '4':
        if number2 == 0:
            print("Division by zero error!")
        else:
            print("Result: ", division(number1, number2))
