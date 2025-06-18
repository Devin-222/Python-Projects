# List of VIP guests
vip = ["Thomas", "Costa", "Jon"]
vip_total = len(vip)  # Total number of VIPs

guest_max = 5  # Maximum number of guests allowed

guests = []  # List to store all entered guests
guests_total = len(guests)  # Total number of guests currently inside
vip_entered = 0  # Counter for VIPs who have entered

# Title banner for the security check
title = "-Security Check-"
print("-" * len(title))
print(title)
print("-" * len(title))

# Loop until the guest limit is reached
while guests_total < guest_max:
    # Ask for the guest's name
    name = input("What's your name: ")
    name = name.capitalize()  # Capitalize the name for consistency

    # Check for invalid input: empty or non-alphabetic name
    if name == "" or name.isalpha() == False:
        print("I need a real name.")
    
    # Check if the guest is on the VIP list
    elif name in vip:
        guests.append(name)
        guests_total += 1
        vip_entered += 1  # Count how many VIPs have entered
        print(f"Welcome to the party {name}! Go right in.")
    
    # If the name is not on the VIP list
    elif name not in vip:
        # Check if allowing this guest still leaves room for remaining VIPs
        if guests_total + (vip_total - vip_entered) < guest_max:
            guests.append(name)
            guests_total += 1
            print(f"You're not on the list {name}, but go in.")
        else:
            print(f"Sorry {name}, there are only spaces for VIP guests.")

# Print message when the guest limit is reached
message = "No more guests allowed"
print("-" * len(message))
print(message)
print("-" * len(message))

# Display the final guest list
print("Party Guests:")
guests.sort()  # Sort the guest list alphabetically
for names in guests:
    print(names)
print("Total:", guests_total)
