# Challenge:
# Boolean logic with operators only — no if/else
# A year is a leap year if:
# • it is divisible by 4, AND
# • it is NOT divisible by 100, UNLESS it is also divisible by 400.

# Take a year from the user. WITHOUT using if/else, print each individual condition's boolean result, then the final combined answer built purely from boolean operators (and / or / not).

# Example (year = 2000):
# Divisible by 4:   True
# Divisible by 100: True
# Divisible by 400: True
# Is leap year:     True

# Example (year = 1900):
# Divisible by 4:   True
# Divisible by 100: True
# Divisible by 400: False
# Is leap year:     False

# Solution:
year = int(input("Enter a year:"))
is_divisible_by_4 = year % 4 == 0
is_divisible_by_100 = year % 100 == 0
is_divisible_by_400 = year % 400 == 0

leap_year = is_divisible_by_4 and (not is_divisible_by_100 or is_divisible_by_400)

print("Divisible by 4:",is_divisible_by_4)
print("Divisible by 100:",is_divisible_by_100)
print("Divisible by 400:",is_divisible_by_400)
print(leap_year)