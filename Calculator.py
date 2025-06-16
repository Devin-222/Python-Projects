print("""Calculator:
+---------+
0
+---------+
| [+] [-] |
| [*] [/] |
+---------+
""")

num1 = float(input("First number: "))
operator = input("Enter operator: ")
num2 = float(input("Second number: "))

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

print("Answer:")
print("+---------+")
print(total)
print("+---------+")
