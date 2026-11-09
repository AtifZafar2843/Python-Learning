# Challenge:
# Storing values in variables and reusing them
# Build a simple interest calculator driven by variables.
# Define three variables: principal, rate (percent per year), and time (in years). Then calculate:
# • Simple Interest:  SI = (principal × rate × time) / 100
# • Total amount:     principal + SI
# Print both results with a clear label.

# Example (principal = 1000, rate = 5, time = 2):
# Simple Interest: 100.0
# Total Amount: 1100.0
# Now change principal to a new value at the top and run again — notice that only ONE line changes, but both results update. That is the whole point of variables.

# Solution:
#Example 1 with 1000 as principle and 5 percent as rate
principle = 1000
rate = 5
time = 2

SI = (principle * rate * time) / 100
total_amount = principle + SI

print("Simple Interest:",SI)
print("Total Amount:",total_amount)

#Example 2 with 5000 as principle and 10 percent as rate
principle = 5000
rate = 10
time = 2

SI = (principle * rate * time) / 100
total_amount = principle + SI

print("Simple Interest:",SI)
print("Total Amount:",total_amount)