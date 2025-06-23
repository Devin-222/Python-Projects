# While loop to allow the user to do another calculation if they choose to do so
while True:
    # Calculator display
    print("""
Calculator:
+---------+
0
+---------+
| [+] [-] |
| [*] [/] |
+---------+
""")

    # User input for the two numbers to be operated on and the operator to be used
    num1 = float(input("First number: "))

    # Simple operator validator that checks if the input from the user is a valid operator from the tuple
    valid_operators = ("+", "-", "*", "/")
    operator = input(f"Enter operator{valid_operators}: ")
    while operator not in valid_operators:
        print(f"Invalid operator, choose one of the following{valid_operators}: ")
        operator = input("Enter operator: ")
    
    num2 = float(input("Second number: "))

    # Based on the operator that was selected the corresponding operation will take place
    if operator == "+":
        total = num1 + num2
    elif operator == "-":
        total = num1 - num2
    elif operator == "*":
        total = num1 * num2
    elif operator == "/":
        total = num1 / num2
    else:
        total = "Invalid operator"

    print()

    # Display the output of the calculation
    print("Answer:")
    print("+---------+")
    print(total)
    print("+---------+")

    # User is given the option to use the calculator again
    again = input("Calculate again?: ")
    valid_answers = ("Yes", "yes", "Y", "y")

    # If they enter an answer that is not in the tuple then the program will stop
    if again not in valid_answers:
        print("Goodbye!")
        break
