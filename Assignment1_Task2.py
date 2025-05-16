def greet():
    try:
        a = input("Enter your first name: ")
        b = input("Enter your last name: ")
        print("Hello, " + a + " " + b + "! Welcome to the python program.")
    except Exception as e:
        print("An error occurred: ", e)
        return

greet()