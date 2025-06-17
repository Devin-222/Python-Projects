print("""
+-----------------------+
| Website Voucher Codes |
+-----------------------+
""")

website = "www.website.com/"

# Global voucher code counter that persists across batches
code_counter = 0

while True:
    choice = input("Type 'c' to create vouchers or 'q' to quit: ").strip().lower()
    
    if choice == 'q':
        print("Goodbye!")
        break
    elif choice == 'c':
        try:
            # User inputs
            discount_amount = int(input("Discount %: "))
            voucher_amount = int(input("Amount: "))

            # Generate unique voucher codes that continue from last
            for _ in range(voucher_amount):
                print(f"{website}?voucherCode={discount_amount}-{code_counter}")
                code_counter += 1  # Increment global counter

            print()  # Blank line for spacing
        except ValueError:
            print("Invalid input. Please enter numbers for discount and amount.\n")
    else:
        print("Invalid option. Please enter 'c' to continue or 'q' to quit.\n")
