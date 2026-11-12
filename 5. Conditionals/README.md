# 05. Conditionals

This folder covers branching logic in Python—allowing programs to make decisions, validate inputs, and execute different paths based on runtime conditions.

---

## 📌 Topics Overview

### 1. `if` / `elif` / `else` Blocks
- **`if`**: Evaluates a condition. If `True`, its indented block runs.
- **`elif` (else if)**: Checked only if previous `if` or `elif` statements evaluated to `False`.
- **`else`**: The fallback block that executes if none of the preceding conditions were met.
  ```python
  if score >= 90:
      grade = "A"
  elif score >= 75:
      grade = "B"
  else:
      grade = "C"
  ```

### 2. Nested Conditions vs. Flattening Logic
- **Nested Conditions:** Placing `if` statements inside another `if` block. Deep nesting ("pyramid of doom") makes code hard to read and debug.
- **Flattening Logic:** Checking guard clauses (e.g., input errors) early and using compound logical operators (`and` / `or`) keeps code flat, clean, and maintainable:
  ```python
  # Flat & Clean
  if marks < 0 or marks > 100:
      print("Invalid marks")
  ```

### 3. Ternary Expressions (Conditional One-Liners)
- Concise syntax for assigning a value based on a condition:
  ```python
  status = "Pass" if marks >= 40 else "Fail"
  ```

### 4. Booleans as Integers in Python
- In Python, `bool` is a subclass of `int` where `True == 1` and `False == 0`.
- This enables clean scoring logic by adding boolean flags together (e.g., `score = cond1 + cond2 + cond3`).

---

## 🎯 Challenges & Solutions

### 🔹 Challenge 1: Grading System & Input Validation (`challenge1.py`)
- **Objective:** Ask user for marks out of 100. Check bounds (0–100), assign grade (A: 90–100, B: 75–89, C: 60–74, D: 40–59, Fail: < 40), and print whether the student passed ($\ge 40$).
- **My Solution:**
  ```python
  marks = int(input("Enter your marks Out of 100: "))

  if (marks <= 0 or marks >= 100):
      print("Invalid Input")

  if (marks >= 90 and marks <= 100):
      print("Grade: A")
  elif (marks >= 75 and marks <= 89):
      print("Grade: B")
  elif (marks >= 60 and marks <= 74):
      print("Grade: C")
  elif (marks >= 40 and marks <= 59):
      print("Grade: D")
  elif (marks >= 0 and marks <= 39):
      print("Fail")

  if marks >= 40:
      print("Pass")
  ```
- **What I Learned & How I Solved It:**
  - Handled input validation first before processing grade ranges.
  - Used chained comparisons to match exact ranges.
  - Kept the "Pass" status check independent of the letter grade so both are displayed accurately.

---

### 🔹 Challenge 2: Cinema Ticket Price Engine (`challenge2.py`)
- **Objective:** Calculate ticket price starting at Rs 200 base price with consecutive rules:
  - Age $\le 12$ or $> 60$: 50% discount on base price.
  - Student (`"yes"`): 20% discount on base price.
  - Weekend (`"saturday"` or `"sunday"`): 50% surcharge applied **after** discounts.
- **My Solution:**
  ```python
  age = int(input("enter your age: "))
  is_student = input("Are you a student? (yes/no): ")
  day = input("enter the day: ")

  ticket_price = 200
  age_discount = ticket_price / 2
  student_discount = (ticket_price * 20) / 100

  if age <= 12 or age > 60:
      print(f"Age Discount: Rs -{ticket_price / 2}")
      ticket_price -= age_discount

  if is_student == "yes":
      print(f"Student Discount: Rs -{student_discount}")
      ticket_price -= student_discount

  if day == "saturday" or day == "sunday":
      week_surcharge = (ticket_price * 50) / 100
      print(f"Weekend Surcharge: Rs +{week_surcharge}")
      ticket_price += week_surcharge

  print(f"Final Ticket Price: {ticket_price}")
  ```
- **What I Learned & How I Solved It:**
  - Order of operations in business logic: discounts were deducted first, and the weekend surcharge was computed on the remaining subtotal.
  - Used `+=` and `-=` assignment operators to adjust running totals dynamically.

---

### 🔹 Challenge 3: Password Strength Checker (`challenge3.py`)
- **Objective:** Evaluate password strength against 5 rules (Length $\ge 8$, Uppercase, Lowercase, Number, Special Character). Rate password as Weak ($\le 2$), Medium ($3 - 4$), or Strong ($5$).
- **My Solution:**
  ```python
  password = input("Enter you password: ")

  pass_length = len(password) >= 8
  has_upper = password != password.lower()
  has_lower = password != password.upper()
  has_number = any(ch in password for ch in "0123456789")
  has_sp_char = any(ch in password for ch in "!@#$%^&*()-=+_|/?")

  # Add booleans directly as integers (True = 1, False = 0)
  pass_score = pass_length + has_upper + has_lower + has_number + has_sp_char

  if pass_score <= 2:
      rating = "weak"
  elif pass_score <= 4:
      rating = "Medium"
  else:
      rating = "Strong"

  print(f"Password Strength: {rating} ({pass_score}/5)")
  ```
- **What I Learned & How I Solved It:**
  - Evaluated character presence without regex by comparing `.lower()` / `.upper()` and substring searches.
  - Used boolean addition (`True + True` $\rightarrow$ `2`) as an elegant scoring engine.
  - Converted the numerical score into descriptive categories (`Weak`, `Medium`, `Strong`) using `if/elif/else`.

