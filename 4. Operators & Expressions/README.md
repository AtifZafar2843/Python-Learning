# 04. Operators & Expressions

This folder focuses on going beyond simple math in Python. It covers comparison operators, compound boolean logic, truthy/falsy evaluation, operator precedence, and low-level bitwise operations.

---

## 📌 Topics Overview

### 1. Arithmetic Operators
- `+` (Addition), `-` (Subtraction), `*` (Multiplication)
- `/` (True Float Division: `7 / 2` $\rightarrow$ `3.5`)
- `//` (Floor Division: `7 // 2` $\rightarrow$ `3`)
- `%` (Modulo: Returns division remainder: `7 % 2` $\rightarrow$ `1`)
- `**` (Exponentiation / Power: `2 ** 3` $\rightarrow$ `8`)

### 2. Comparison Operators
Always return a boolean (`True` or `False`):
- `==` (Equal to) and `!=` (Not equal to)
- `>` (Greater than) and `<` (Less than)
- `>=` (Greater than or equal to) and `<=` (Less than or equal to)

### 3. Logical Operators (`and`, `or`, `not`)
- **`and`**: Returns `True` only if **both** conditions are `True`.
- **`or`**: Returns `True` if **at least one** condition is `True`.
- **`not`**: Reverses the boolean truth value (`not True` $\rightarrow$ `False`).

### 4. Truthy & Falsy Values
In Python, values in a boolean context naturally evaluate to `True` or `False`:
- **Falsy values:** `0`, `0.0`, `""` (empty string), `None`, `[]` (empty list), `False`.
- **Truthy values:** Any non-zero number (e.g., `1`, `-5`), non-empty strings (`"hello"`), and populated collections.
- **Short-Circuit Evaluation:**
  - `x or y`: Returns `x` if `x` is truthy, otherwise returns `y`.
  - `x and y`: Returns `x` if `x` is falsy, otherwise evaluates and returns `y`.

### 5. Operator Precedence (PEMDAS / Order of Operations)
1. Parentheses: `()`
2. Exponentiation: `**`
3. Multiplication, Division, Modulo: `*`, `/`, `//`, `%`
4. Addition & Subtraction: `+`, `-`
5. Comparisons: `==`, `!=`, `<`, `>`, `<=`, `>=`
6. Logical `not`
7. Logical `and`
8. Logical `or`

### 6. Bitwise Operators
Direct manipulation of numbers at their binary bit level:
- `&` (Bitwise AND), `|` (Bitwise OR), `^` (Bitwise XOR)
- `<<` (Left Shift: doubles value per shift), `>>` (Right Shift: halves value per shift)
- `bin()`: Built-in function to view the binary representation (e.g., `bin(5)` $\rightarrow$ `'0b101'`).

---

## 🎯 Challenges & Solutions

### 🔹 Challenge 1: Number Relationship & Modulo (`challenge1.py`)
- **Objective:** Take two numbers from the user and output:
  1. Which number is larger.
  2. The remainder of `num1 / num2`.
  3. Whether the numbers are both even, both odd, or mixed.
- **My Solution:**
  ```python
  num1 = int(input("Enter number 1:"))
  num2 = int(input("Enter number 2:"))

  # Short-circuit logic to pick larger without if/else
  larger_num = (num1 > num2 and num1) or num2

  print("larger:", larger_num)
  print(f"Remainder of {num1} / {num2}: {num1 % num2}")

  num1_even = num1 % 2 == 0
  num2_even = num2 % 2 == 0

  both_even = (num1_even and num2_even)
  both_odd = (not num1_even and not num2_even)
  mixed = (not both_even and not both_odd)

  both_even and print("Both even")
  both_odd and print("Both odd")
  mixed and print("mixed")
  ```
- **What I Learned & How I Solved It:**
  - Used modulo `% 2 == 0` to check evenness.
  - Leveraged Python's short-circuit `and` / `or` evaluation to conditionally store values and trigger `print()` statements without traditional `if` blocks.

---

### 🔹 Challenge 2: Leap Year Logic with Pure Boolean Operators (`challenge2.py`)
- **Objective:** Determine if a year is a leap year without using `if/else`. A leap year is divisible by 4 AND (not divisible by 100 UNLESS also divisible by 400).
- **My Solution:**
  ```python
  year = int(input("Enter a year:"))
  is_divisible_by_4 = year % 4 == 0
  is_divisible_by_100 = year % 100 == 0
  is_divisible_by_400 = year % 400 == 0

  leap_year = is_divisible_by_4 and (not is_divisible_by_100 or is_divisible_by_400)

  print("Divisible by 4:", is_divisible_by_4)
  print("Divisible by 100:", is_divisible_by_100)
  print("Divisible by 400:", is_divisible_by_400)
  print("Is leap year:", leap_year)
  ```
- **What I Learned & How I Solved It:**
  - Broke down a complex real-world rule into separate, readable boolean variables.
  - Combined them using `and`, `or`, and `not` with parentheses to enforce proper precedence.

---

### 🔹 Challenge 3: Bitwise Explorer (`challenge3.py`)
- **Objective:** Take two numbers (`a = 5`, `b = 3`) and inspect how the computer operates on their binary representation using AND, OR, XOR, left shift, and right shift.
- **My Solution:**
  ```python
  a = 5  # 0b101
  b = 3  # 0b011

  and_res = a & b          # 1  (0b001)
  or_res = a | b           # 7  (0b111)
  xor_res = a ^ b          # 6  (0b110)
  left_shift_res = a << 1  # 10 (0b1010)
  right_shift_res = a >> 1 # 2  (0b10)

  print(f"a = {a}")
  print(f"b = {b}")
  print(f"a & b = {and_res} ({bin(and_res)})")
  print(f"a | b = {or_res} ({bin(or_res)})")
  print(f"a ^ b = {xor_res} ({bin(xor_res)})")
  print(f"a << 1 = {left_shift_res} ({bin(left_shift_res)})")
  print(f"a >> 1 = {right_shift_res} ({bin(right_shift_res)})")
  ```
- **What I Learned & How I Solved It:**
  - Explored how integers are stored as binary bits.
  - Understood how `<< 1` shifts bits left (multiplying by 2) and `>> 1` shifts bits right (integer division by 2).
  - Used `bin()` to visually verify the underlying bit manipulations.

