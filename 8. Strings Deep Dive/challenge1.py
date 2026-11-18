# Challenge:
# Ask for a full name and produce:
# • The first name and last name separately
# • The initials (e.g. "Rahul Kumar Sharma" -> "R.K.S.")
# • The name in Title Case

# Handle names of any length — two words, three words, or more.

# Example:
# Full name: rahul kumar sharma
# First: rahul
# Last: sharma
# Initials: R.K.S.
# Title Case: Rahul Kumar Sharma

# Hint: split() turns the name into a list of words you can index and loop over.

# Solution:
user_name = input("Enter your full name: ")
print(f"Name: {user_name}")

split_name = user_name.split()

first_name = split_name[0]
middle_name = split_name[1]
last_name = split_name[2]

print(f"First Name: {first_name}")
print(f"Middle Name: {middle_name}")
print(f"Last Name: {last_name}")
print(f"Initials: {first_name[0].upper()}.{middle_name[0].upper()}.{last_name[0].upper()}.")
print(f"Title Case: {user_name.title()}")
