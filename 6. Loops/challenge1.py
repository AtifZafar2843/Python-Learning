# Challenge:
# for loops and range()
# Ask the user for a number and print its multiplication table from 1 to 10 using a loop.

# Example (number = 7):
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# ...
# 7 x 10 = 70

# Use a for loop with range(1, 11) so you write the print line only once.


# Solution:
table_num = int(input("Enter a number for Table: "))

for i in range(1, 11):
    print(f"{table_num} X {i} = {i*table_num}")