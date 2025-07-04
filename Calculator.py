# Display a simple text-based calculator UI
def display_calc():
    print("""
Calculator:
+---------+
0
+---------+
| [+] [-] |
| [*] [/] |
+---------+
""")

# Handle user input for numbers and operator, with validation
def user_inputs():
    num1 = float(input("First number: "))

    # Define allowed operators
    valid_operators = ("+", "-", "*", "/")
    operator = input(f"Enter operator{valid_operators}: ")
    
    # Re-prompt until a valid operator is given
    while operator not in valid_operators:
        print(f"Invalid operator, choose one of the following{valid_operators}: ")
        operator = input("Enter operator: ")
    
    num2 = float(input("Second number: "))

    # Perform the calculation
    calculate(num1, operator, num2)

# Perform the calculation based on operator and print result in a box
def calculate(num1, operator, num2):
    if operator == "+":
        total = num1 + num2
    elif operator == "-":
        total = num1 - num2
    elif operator == "*":
        total = num1 * num2
    elif operator == "/":
        total = num1 / num2
    else:
        total = "Invalid operator"  # Fallback — though unreachable with input validation

    print()
    print("Answer:")
    print("+---------+")
    print(total)
    print("+---------+")

# Ask user if they want to calculate again, return True/False
def calc_again():
    again = input("Calculate again?: ")
    valid_answers = ("Yes", "yes", "Y", "y")

    if again not in valid_answers:
        print("Goodbye!")
        return False

# Main program loop
while True:
    display_calc()
    user_inputs()
    again = calc_again()
    if again == False:
        break
