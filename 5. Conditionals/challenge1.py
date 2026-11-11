# Challenge:
# if/elif/else chains and input validation
# Ask the user for marks out of 100 and print a grade:
# • 90–100 -> A
# • 75–89  -> B
# • 60–74  -> C
# • 40–59  -> D
# • below 40 -> Fail

# Also print whether the student passed (40 or above). If the marks are less than 0 or greater than 100, print an "Invalid input" message instead of a grade.

# Example:
# Enter marks (0-100): 82
# Grade: B
# Status: Pass

# Solution:
marks = int(input("Enter your marks Out of 100: "))

if (marks <= 0 or marks >= 100):
    print("Invalid Input")

if (marks >= 90 and marks <= 100):
    print("Grade: A")
elif (marks >= 75 and marks <= 89):
    print("Grade: B")
elif (marks >= 60 and marks <= 74):
    print("Grade: C")
elif (marks >= 40 and marks <=  59):
    print("Grade: D")
elif (marks >= 0 and marks <= 39):
    print("Fail")

if(marks >= 40):
    print("Pass")