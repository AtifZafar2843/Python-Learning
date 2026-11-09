# 01. Python Basics

Welcome to my first steps in Python! This folder contains my initial hands-on practice with writing Python code, understanding how Python runs instructions, and solving basic logic challenges.

---

## 📌 Topics Overview

### 1. `print()`
- The `print()` function is used to display output on the screen/console.
- It can print plain text strings (enclosed in `" "` or `' '`), numbers, and results of mathematical operations.
- Multiple values can be printed in a single `print()` call separated by commas (`,`), which automatically adds a space between them.

### 2. Comments (`#`)
- Any text starting with `#` is ignored by Python during execution.
- Used to explain what the code does, document problems/solutions, and temporarily disable lines while testing.

### 3. Execution Order
- Python is an interpreted language that runs code **line-by-line from top to bottom**.
- Order matters: a line cannot use something that hasn't been defined in a previous line.

### 4. Error Messages
- Errors are not failures; they are debugging guides.
- Python traceback indicates the file name, the exact line number, and the error type (e.g., `SyntaxError`, `NameError`), pointing directly to what needs fixing.

---

## 🎯 Challenges & Solutions

### 🔹 Challenge 1: Self Introduction & Dynamic Age Math (`challenge1.py`)
- **Objective:** Print name, age, city, and dynamically calculate the birth year using the current year (2026) and age inside `print()` without hardcoding the year.
- **My Solution:**
  ```python
  print("Atif")
  print(22)
  print("Aligarh, Uttar Pradesh")
  print("I was born in", 2026 - 22)
  ```
- **What I Learned & How I Solved It:**
  - Learned how to mix strings and mathematical expressions in a single `print()` statement using comma separation.
  - Python automatically computes `2026 - 22` first and prints the resulting value (`2004`) alongside the text.

---

### 🔹 Challenge 2: Store Receipt Formatting & In-Print Math (`challenge2.py`)
- **Objective:** Design a neat shopping receipt for a store ("ATIF STORE") listing 3 items with prices, separator lines, and a calculated `TOTAL` at the bottom using arithmetic inside `print()`.
- **My Solution:**
  ```python
  print("==== ATIF STORE ====")
  print("Notebook      Rs 60")
  print("Pen           Rs 15")
  print("Eraser        Rs 5")
  print("--------------------")
  print("TOTAL         Rs", 60 + 15 + 5)
  ```
- **What I Learned & How I Solved It:**
  - Practiced manual string alignment and clean console formatting using dashes and spacing.
  - Combined multiple additions (`60 + 15 + 5`) directly inside `print()` to produce dynamic totals instead of static hardcoded numbers.

---

### 🔹 Challenge 3: Visual Shape Drawing with Print (`challenge3.py`)
- **Objective:** Draw two shapes using only `print()` and asterisk characters `*` (no loops or variables):
  1. A 5x5 hollow square (stars on borders, spaces inside).
  2. A 5-row right-angled triangle.
- **My Solution:**
  ```python
  # 1) Hollow 5x5 Square
  print("*****")
  print("*   *")
  print("*   *")
  print("*   *")
  print("*****")

  # 2) Right-angled Triangle
  print("*")
  print("**")
  print("***")
  print("****")
  print("*****")
  ```
- **What I Learned & How I Solved It:**
  - Understood how Python's line-by-line execution prints each line sequentially with automatic newline characters.
  - Learned to visualize patterns row by row, carefully aligning spaces for the hollow inner region of the square.

