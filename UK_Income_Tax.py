# Setting up the tax thresholds and rates based on UK tax brackets
personal_allowance = 12_500                  # Tax-free income threshold
personal_allowance_limit = 100_000           # Threshold after which allowance is reduced

basic_band = 37_500                          # Income up to this is taxed at basic rate
higher_band = 150_000                        # Income up to this is taxed at higher rate

basic_rate = 0.2                             # 20% tax
higher_rate = 0.4                            # 40% tax
additional_rate = 0.45                       # 45% tax for income above £150,000

print(" - Income Tax Calculator - ")

# Ask user for their annual salary
salary = float(input("Enter annual salary: "))

# Reduce personal allowance for salaries above £100,000
if salary > personal_allowance_limit:
    personal_allowance -= (salary - personal_allowance_limit) / 2
    if personal_allowance < 0:
        personal_allowance = 0  # No allowance if income is too high

# Calculate the taxable portion of the salary
taxable_income = salary - personal_allowance

# Determine tax owed based on brackets
if taxable_income <= 0:
    tax = 0
elif taxable_income <= basic_band:
    tax = taxable_income * basic_rate
elif taxable_income <= higher_band:
    # Basic rate on first £37,500, higher rate on the rest
    tax = (basic_band * basic_rate) + ((taxable_income - basic_band) * higher_rate)
else:
    # Basic rate on first £37,500, higher rate on next portion, additional rate on remainder
    tax = ((basic_band * basic_rate) + ((higher_band - basic_band) * higher_rate) + ((taxable_income - higher_band) * additional_rate))

# Round the tax to two decimal places
year_tax = round(tax, 2)
monthly_tax = round(tax / 12, 2)

# Display the result
print(f"Your income tax yearly is £{year_tax} and monthly is £{monthly_tax}.")
