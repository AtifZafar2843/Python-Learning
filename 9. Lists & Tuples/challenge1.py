# Challenge:
# Read 5 numbers into a list. WITHOUT using the built-in sum(), min(), or max(), compute and print:
# • the list sorted in ascending order
# • the list reversed
# • the sum
# • the average
# • the maximum and the minimum

# Example:

# Numbers: [42, 17, 8, 99, 23]
# Sorted: [8, 17, 23, 42, 99]
# Reversed: [23, 99, 8, 17, 42]
# Sum: 189
# Average: 37.8
# Max: 99, Min: 8

# Compute the sum, max, and min yourself with a loop — that's the learning goal here.

# Solution:
numbers = []
for i in range(1, 6):
  num = int(input(f"Enter number {i}:"))
  numbers.append(num)

sorted_numbers = sorted(numbers)
copied_numbers = numbers.copy()
copied_numbers.reverse()

sum = 0
minimum_number = numbers[0]
maximum_number = numbers[0]

for num in numbers:
  sum += num

for num in numbers:
  if num > maximum_number:
    maximum_number = num

for num in numbers:
  if num < minimum_number:
    minimum_number = num

print(f"Numbers: {numbers}")
print(f"Sorted: {sorted_numbers}")
print(f"Reversed: {copied_numbers}")
print(f"Sum: {sum}")
print(f"Average: {sum / len(numbers)}")
print(f"Max: {maximum_number}, Min: {minimum_number}")
