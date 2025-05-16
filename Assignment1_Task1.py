def arithmetic_Operations():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return
    print("Addition: ", a + b)
    print("Subtraction: ", a - b)  
    print("Multiplication: ", a * b)
    print("Division: ", a / b)

arithmetic_Operations()