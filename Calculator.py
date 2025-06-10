print("""Calculator:
+---------+
0
+---------+
| [+] [-] |
| [*] [/] |
+---------+
""")

num1 = float(input("First number: "))
print("Operator: +")
num2 = float(input("Second number: "))
total = num1 + num2

print()

print("Answer:")
print("+---------+")
print(total)
print("+---------+")
