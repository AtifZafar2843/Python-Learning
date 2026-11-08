# Challenge:
# Multiple inputs feeding a real-world formula
# Ask the user for a loan amount, an annual interest rate (percent), and a tenure in months. Compute the monthly EMI (equated monthly instalment).

# Formula:
# r = (annual_rate / 12) / 100          # monthly rate as a decimal
# EMI = P * r * (1 + r)**n / ((1 + r)**n - 1)
# where P is the loan amount and n is the number of months.

# Print the EMI rounded to 2 decimal places.

# Example:
# Loan amount: 500000
# Annual interest rate (%): 8.5
# Tenure (months): 60
# Monthly EMI: Rs 10258.27

# Solution:
# Take input from user
loan_amount = int(input("Enter the loan Amount:"))
annual_interest_rate = float(input("Enter the Annual Interest Rate (%):"))
tenure = int(input("Enter the Tenure (months):"))

monthly_interest_rate = (annual_interest_rate / 12) / 100
EMI = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate)**tenure / ((1 + monthly_interest_rate)**tenure - 1)

print("Loan Amount:",loan_amount)
print("Annual Interest Rate (%):",annual_interest_rate)
print("Tenure (months):",tenure)
# I am using built-in function here for 2 decimal places.
print("Monthly EMI:", round(EMI, 2))