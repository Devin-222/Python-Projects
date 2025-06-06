import math

# Function to find the hypotenuse
def find_hypotenuse(adjacent, opposite):
    return math.sqrt(adjacent ** 2 + opposite ** 2)

# Function to find the opposite side
def find_opposite(hypotenuse, adjacent):
    return math.sqrt(hypotenuse ** 2 - adjacent ** 2)

# Function to find the adjacent side
def find_adjacent(hypotenuse, opposite):
    return math.sqrt(hypotenuse ** 2 - opposite ** 2)

# Main interactive calculator
def pythagoras_calculator():
    print()
    print("Welcome to the Pythagoras Calculator!")

    while True:
        option = input("""
Which side do you want to find?
- Hypotenuse - hyp
- Opposite - opp
- Adjacent - adj

To quit the program enter 'q'
""").strip().lower()
        
        if option == 'q':
            break

        try:
            if option in ["hypotenuse", "hyp"]:
                a = input("Enter the adjacent side length: ")
                if a.lower() == 'q': break
                b = input("Enter the opposite side length: ")
                if b.lower() == 'q': break
                result = find_hypotenuse(float(a), float(b))
                print("----------------------------------")
                print(f"The hypotenuse is: {result:.2f}")
                print("----------------------------------")

            elif option in ["opposite", "opp"]:
                c = input("Enter the hypotenuse length: ")
                if c.lower() == 'q': break
                a = input("Enter the adjacent side length: ")
                if a.lower() == 'q': break
                result = find_opposite(float(c), float(a))
                print("----------------------------------")
                print(f"The opposite side is: {result:.2f}")
                print("----------------------------------")

            elif option in ["adjacent", "adj"]:
                c = input("Enter the hypotenuse length: ")
                if c.lower() == 'q': break
                b = input("Enter the opposite side length: ")
                if b.lower() == 'q': break
                result = find_adjacent(float(c), float(b))
                print("----------------------------------")
                print(f"The adjacent side is: {result:.2f}")
                print("----------------------------------")

            else:
                print("""
Invalid choice. Please choose one of the following:
- Hypotenuse - hyp
- Opposite - opp
- Adjacent - adj

To exit the program enter 'q'
""")

        except ValueError:
            print("Invalid input. Please enter numeric values only.\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

    print("Goodbye! Thanks for using the Pythagoras Calculator.")

# Run the calculator
if __name__ == "__main__":
    pythagoras_calculator()
