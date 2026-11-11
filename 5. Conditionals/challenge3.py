# Challenge:


# Solution:
password = input("Enter you password: ")

pass_length = len(password) >=8
has_upper = password != password.lower()
has_lower = password != password.upper()
has_number = (
    "0" in password or
    "1" in password or
    "2" in password or
    "3" in password or
    "4" in password or
    "5" in password or
    "6" in password or
    "7" in password or
    "8" in password or
    "9" in password
)
has_sp_char = (
    "!" in password or
    "@" in password or
    "#" in password or
    "$" in password or
    "%" in password or
    "^" in password or
    "&" in password or
    "*" in password or
    "(" in password or
    ")" in password or
    "-" in password or
    "=" in password or
    "+" in password or
    "_" in password or
    "|" in password or
    "/" in password or
    "/?" in password
)

pass_score = pass_length + has_upper + has_lower + has_number + has_sp_char

if pass_length:
    print(f"Length >= 8: Yes")
else:
    print(f"Length >= 8: No")
if has_upper:
    print(f"Has Uppercase: Yes")
else:
    print(f"Has Uppercase: No")
if has_lower:
    print(f"Has Lowercase: Yes")
else:
    print(f"Has Lowercase: No")
if has_number:
    print(f"Has Number: Yes")
else:
    print(f"Has Number: No")
if has_sp_char:
    print(f"Has Special Character: Yes")
else:
    print(f"Has Special Character: No")
    
if pass_score <= 2:
    rating = "weak"
elif pass_score <=4:
    rating = "Medium"
else:
    rating = "Strong"
    
print(f"Password Strength: {rating} ({pass_score}/5)")
