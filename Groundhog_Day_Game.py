# Modules
import time

# Number the user has to guess
perfect_num = 12_395

# Clock faces based on the movie Groundhog day
clock1 = """
+---+---+---+
| 5 | 5 | 9 |
+---+---+---+
"""

clock2 = """
+---+---+---+
| 6 | 0 | 0 |
+---+---+---+
"""

# Game instructions
print("""
+-----------------------------------+
| Welcome to Groundhog Day - 2 Feb. |
| You're stuck in 2 Feburary 2020.  |
| Enter the perfect number to end   |
| the loop or be stuck forever...   |
+-----------------------------------+
""")

num = int(input("Enter number: "))

# Loop to ask for new input till the perfect number is entered
while num != perfect_num:
    if num < perfect_num:
        print(clock1)
        time.sleep(1)
        print(clock2)
        time.sleep(1)
        print("Februrary 2\nNumber too low.\n")
    else:
        print(clock1)
        time.sleep(1)
        print(clock2)
        time.sleep(1)
        print("Februrary 2\nNumber too high.\n")

    num = int(input("Enter number: "))

# Prints the clock and tells the user that they have escaped the loop
print(clock1)
time.sleep(1)
print(clock2)
time.sleep(1)
print("Februrary 3\nToday is tomorrow.\nCongratulations, you have escaped the loop.\n")
