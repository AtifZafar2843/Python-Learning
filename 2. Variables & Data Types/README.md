# 02. Variables & Data Types

This folder covers how Python stores information in memory, how data types work, and how variables enable reusable, dynamic code.

---

## 📌 Topics Overview

### 1. Variables
- Variables are named containers used to store data values in memory.
- You create a variable the moment you assign a value to it using the assignment operator (`=`):
  ```python
  age = 22
  name = "Atif"
  ```

### 2. Core Data Types (`int`, `float`, `str`, `bool`)
- **`int`**: Whole numbers without decimals (e.g., `10`, `-5`, `0`).
- **`float`**: Numbers with decimal points (e.g., `3.14`, `100.0`, `0.621`).
- **`str`**: Text wrapped in single (`'...'`) or double (`"..."`) quotes.
- **`bool`**: Boolean values representing truth states: `True` or `False`.

### 3. `type()` Function
- Used to inspect and verify the data type of any variable or value:
  ```python
  type(100)       # <class 'int'>
  type(3.14)      # <class 'float'>
  type("Python")  # <class 'str'>
  ```

### 4. Variable Reassignment
- Variables in Python are dynamically typed and mutable in reference.
- You can change the value of a variable at any time; assigning a new value overwrites whatever was stored previously.

### 5. Naming Conventions (Best Practices)
- Use descriptive names in `snake_case` (e.g., `total_amount`, `loan_amount`, `monthly_rate`).
- Names cannot begin with numbers (e.g., `1var` is invalid; use `var_1`).
- Avoid reserved keywords (like `print`, `type`, `class`, `for`, `def`).

---

## 🎯 Challenges & Solutions

### 🔹 Challenge 1: Simple Interest & Total Amount Calculator (`challenge1.py`)
- **Objective:** Calculate Simple Interest (`SI = (P × R × T) / 100`) and the Total Amount (`P + SI`) using variables. Demonstrate how changing initial values once updates all downstream calculations.
- **My Solution:**
  ```python
  # Example 1
  principle = 1000
  rate = 5
  time = 2

  SI = (principle * rate * time) / 100
  total_amount = principle + SI

  print("Simple Interest:", SI)
  print("Total Amount:", total_amount)

  # Example 2: Reassigning principle and rate
  principle = 5000
  rate = 10
  time = 2

  SI = (principle * rate * time) / 100
  total_amount = principle + SI

  print("Simple Interest:", SI)
  print("Total Amount:", total_amount)
  ```
- **What I Learned & How I Solved It:**
  - Understood the core advantage of variables: logic is written once, and only the input variables need changing.
  - Division (`/`) in Python always returns a `float` (e.g., `100.0`), showing how Python automatically handles numeric types during arithmetic.

---

### 🔹 Challenge 2: Single Source Unit Converter (`challenge2.py`)
- **Objective:** Store a single distance in kilometers (`km`) and derive multiple units (miles, meters, centimeters, feet), each stored in its own variable.
- **My Solution:**
  ```python
  km = 5
  miles = km * 0.621
  meters = km * 1000
  centimeters = km * 100000
  feet = km * 3280.84

  print("5 km equals:")
  print("   Miles:      ", miles)
  print("   Meters:     ", meters)
  print("   Centimeters:", centimeters)
  print("   Feet:       ", feet)
  ```
- **What I Learned & How I Solved It:**
  - Implemented the "single source of truth" principle: one base variable (`km`) drives all derived calculations.
  - Changing `km = 5` to `km = 285` automatically scales every derived metric correctly without having to touch the formulas.

---

### 🔹 Challenge 3: Value Rotation & Assignment Sequence (`challenge3.py`)
- **Objective:** Rotate three variables `a = 10`, `b = 20`, `c = 30` so that:
  - `a` takes `b`'s value (`20`)
  - `b` takes `c`'s value (`30`)
  - `c` takes `a`'s original value (`10`)
  - Rules: Do not hardcode numbers after setup and explain why assignment order matters.
- **My Discovery & Solution:**
  1. **First attempt without temporary storage:**
     ```python
     a = b  # a becomes 20 (original value 10 is lost!)
     b = c  # b becomes 30
     c = a  # c becomes 20 because 'a' was already 20!
     print(a, b, c)  # Output: 20 30 20 (Incorrect)
     ```
  2. **Final working solution with `temp` variable:**
     ```python
     temp = a  # Save original value of 'a' (10)
     a = b     # a becomes 20
     b = c     # b becomes 30
     c = temp  # c gets original value of 'a' (10)
     print(a, b, c)  # Output: 20 30 10 (Correct!)
     ```
- **What I Learned & How I Solved It:**
  - Realized that assignments in Python happen sequentially. Overwriting a variable without saving its initial value destroys the data forever.
  - Used a third temporary variable (`temp`) to safely hold the original value before reassignment.

