# Challenge:
# Diamond Pattern Generator
# You'll practice
# Nested loops and spacing math
# Ask for an odd number n and print a diamond of stars: n rows in the top half (including the widest middle row), then mirror it for the bottom half.

# Example (n = 3):
#   *
#  ***
# *****
#  ***
#   *
# For each row you need to work out how many leading spaces and how many stars to print. Use loops for both halves — don't hardcode the rows.

# Solution:
n = int(input("Enter an odd number: "))

# 1. TOP HALF (Row 1 se lekar widest row n tak)
for i in range(1, n + 1):
    # Leading spaces print karne ke liye loop
    for s in range(n - i):
        print(" ", end="")
    
    # Stars print karne ke liye loop
    for st in range(2 * i - 1):
        print("*", end="")
    
    # Ek row complete hone ke baad agli line par jaane ke liye
    print()

# 2. BOTTOM HALF (Widest row ke neeche se ulta loop: n-1 se 1 tak)
for i in range(n - 1, 0, -1):
    # Leading spaces print karne ke liye loop
    for s in range(n - i):
        print(" ", end="")
    
    # Stars print karne ke liye loop
    for st in range(2 * i - 1):
        print("*", end="")
    
    # Agli line par jaane ke liye
    print()