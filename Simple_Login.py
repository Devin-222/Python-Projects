# GOALS:
#   Register User:
#       Username:
#           Check if available & 4-20 length
#           Start with letter(alphanumeric only)
#       Password:
#           6 characters minimum
#           Alphanumberic minimum
#       Email:
#           Only 1 @ sign and at least 1 dot
#           10 characters minimum
#           Shouldn't already exist in the system
#   Login:
#       Checks username exists
#       Checks password matches

# Create user database
user_db = {
    "Devin222" : ["abc123", "devin222@email.com"]
}

option = input("""
Menu:
1. Register
2. Login
3. Display dictionary
4. Quit

Select menu option: """)

while option == "1":
    print("\nRegister -")

    while True:
        reg_user = input("\nEnter a username: ")
        reg_user = reg_user.capitalize()

        # Checks entered username with usernames in the user database
        if reg_user in user_db:
            print("Username already exists!")
        # Checks if the username entered is between 4 and 20 characters long
        elif len(reg_user) < 4 or len(reg_user) > 20:
            print("Username must be between 4 - 20 characters!")
        # Checks if the first letter of the username is capitalised
        elif reg_user[0].isalpha() != True:
            print("Username must start with a letter!")
        # Checks if the username contains any characters besides letters and numbers
        elif reg_user.isalnum() == False:
            print("Username can only contain letters and numbers!")
        else:
            break

    while True:
        reg_pass = input("\nEnter password: ")
        # Checks if the password is at least 6 characters
        if len(reg_pass) < 6:
            print("Password must be at least 6 characters!")
        # Checks if the password is only letters or only numbers
        elif reg_pass.isdigit() == True or reg_pass.isalpha() == True:
            print("Password must contain both letters and numbers!")
        else:
            break

    while True:
        reg_email = input("\nEnter email: ")
        reg_email = reg_email.lower()

        for lists in user_db.values():
            # Checks if the email already exists in the user database
            if lists[1] == reg_email:
                print("Email address aleady exists!")
                break
            # Checks if the email inputted has at least 1 @, ., and is at least 10 characters long
            elif reg_email.count("@") != 1 or \
                reg_email.count(".") == 0 or len(reg_email) < 10:
                print("Invalid email address!")
                break
        else:
            break

    # Add the new user to the database
    user_db[reg_user] = [reg_pass, reg_email]

    print(f"{reg_user} registered. You may login now")

    option = input("""
Menu:
1. Register
2. Login
3. Display dictionary
4. Quit

Select menu option: """)
    
while option == "2":
    while True:
        username = input("Enter username: ")
        username = username.capitalize()

        # Check if the username exists in the database
        if username not in user_db:
            print("No such username!")
        else:
            break

    while True:
        password = input("Enter password: ")

        # Checks if the password entered matches the password for that username
        if password != user_db[username][0]:
            print("Incorrect password!")
        else:
            print(f"Welcome {username}!")
            break

# Display the dictionary with all the current data
while option == "3":
    print(user_db)
    break

# Quit the program
while option == "4":
    print("Goodbye!")
    break



