def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero 🤦"
    else:
        return "Invalid operation 🙃"

def main():
    print("Simple Calculator 😉")
    
    try:
        num1 = float(input("1️⃣|Enter the first number: "))
        num2 = float(input("2️⃣|Enter the second number: "))
        print("Choose an operation: ➕,➖,✖️,➗")
        operation = input("Enter the operation: ")
        
        result = calculate(num1, num2, operation)
        print("Result 🟰", result)
    
    except ValueError:
        print("Invalid input. Please enter numeric values for the numbers.")

if __name__ == "__main__":
    main()
