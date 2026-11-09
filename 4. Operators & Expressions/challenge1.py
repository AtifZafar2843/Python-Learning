# challenge:
# Comparison and modulo operators
# Take two numbers from the user and report on their relationship.

# Print:
# • Which number is larger (or whether they are equal)
# • The remainder when the larger is divided by the smaller
# • Whether both are even, both odd, or mixed

# Example:
# Enter first number: 12
# Enter second number: 8
# Larger: 12
# Remainder of 12 / 8: 4
# Both even

# Hint: the modulo operator % gives you the remainder, and a number is even when n % 2 == 0.

# Solution:
# Take two number input from the user
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

# Check and store larger number
larger_num = (num1 > num2 and num1) or num2

print("larger:", larger_num)
print(f"Remainder of {num1} / {num2}: {num1%num2}")

# Placing even number or odd number
num1_even = num1 % 2 == 0
num2_even = num2 % 2 == 0

# according to the sitaution number stores in the both even and both odd or mixed veriable
both_even = (num1_even and num2_even)
both_odd = (not num1_even and not num2_even)
mixed = (not both_even and not both_odd)

# print the even or odd number
both_even and print("Both even")
both_odd and print("Both odd")
mixed and print("mixed")