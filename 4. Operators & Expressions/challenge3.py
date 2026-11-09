# Challenge:
# Bitwise Explorer
# You'll practice
# Binary representation and bitwise operators
# Take two small non-negative integers and explore how the computer sees them in binary.

# For each number, print its binary form. Then show the result of these bitwise operations, each with its binary breakdown: AND (&), OR (|), XOR (^), left shift (<<), and right shift (>>).

# Example (a = 5, b = 3):
# a = 5  -> 0b101
# b = 3  -> 0b011
# a & b  = 1  (0b001)
# a | b  = 7  (0b111)
# a ^ b  = 6  (0b110)
# a << 1 = 10 (0b1010)
# a >> 1 = 2  (0b10)
# Hint: use bin() to get the binary string of a number.

# Solution:
a = 5
b = 3

and_res = a & b
or_res = a | b
xor_res = a ^ b
left_shift_res = a << 1
right_shift_res = a >> 1

print(f"a = {a}")
print(f"b = {b}")
print(f"a & b = {and_res} ({bin(and_res)})")
print(f"a | b = {or_res} ({bin(or_res)})")
print(f"a ^ b = {xor_res} ({bin(xor_res)})")
print(f"a << 1 = {left_shift_res} ({bin(left_shift_res)})")
print(f"a >> 1 = {right_shift_res} ({bin(right_shift_res)})")