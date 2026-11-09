# 03. Input & Type Conversion

This folder covers user interactivity in Python programs using `input()`, converting between data types (type casting), and avoiding common conversion bugs.

---

## 📌 Topics Overview

### 1. `input()` Function
- Enables user interaction by prompting the user for text in the console.
- **Crucial Rule:** `input()` **ALWAYS returns a string (`str`)**, even if the user enters numeric digits like `42` or `3.14`.

### 2. Type Conversion Functions (`int()`, `float()`, `str()`)
- To perform mathematical operations on user input, strings must be explicitly converted:
  - `int()`: Converts integer strings or floats to an integer (e.g., `int("25")` $\rightarrow$ `25`).
  - `float()`: Converts decimal strings or integers to a float (e.g., `float("98.6")` $\rightarrow$ `98.6`).
  - `str()`: Converts any data type back into string format (e.g., `str(100)` $\rightarrow$ `"100"`).

### 3. The Classic "5 + 3 = 53" Bug
- If you add two uncasted `input()` values:
  ```python
  num1 = input("Enter first: ")  # User types 5 -> '5'
  num2 = input("Enter second: ") # User types 3 -> '3'
  print(num1 + num2)             # Output: '53' (String concatenation!)
  ```
- Because both are strings, `+` concatenates them instead of adding mathematically.
- **Fix:** Explicitly wrap with `int()` or `float()`: `int(num1) + int(num2)` $\rightarrow$ `8`.

### 4. Type Casting Errors (`ValueError`)
- Attempting to convert invalid formats causes a `ValueError`:
  - `int("hello")` $\rightarrow$ `ValueError: invalid literal for int() with base 10: 'hello'`
  - `int("3.14")` $\rightarrow$ `ValueError` (must convert with `float("3.14")` first).

---

## 🎯 Challenges & Solutions

### 🔹 Challenge 1: Temperature Converter (`challenge1.py`)
- **Objective:** Prompt user for a temperature in Celsius, convert it to `float`, and calculate its equivalent in both Fahrenheit (`(C × 9/5) + 32`) and Kelvin (`C + 273.15`).
- **My Solution:**
  ```python
  celcius = float(input("Enter temprature in celcius:"))

  fahrenheit = (celcius * 9/5) + 32
  kelvin = celcius + 273.15

  print(celcius, "C =", fahrenheit, "F")
  print(celcius, "C =", kelvin, "K")
  ```
- **What I Learned & How I Solved It:**
  - Since temperatures can be fractional (e.g., `36.6` or `37.5`), `float(input(...))` is essential rather than `int()`.
  - Converted the raw string input immediately upon reading it, allowing smooth arithmetic calculations.

---

### 🔹 Challenge 2: Loan EMI Calculator (`challenge2.py`)
- **Objective:** Ask user for loan amount, annual interest rate (percentage), and tenure in months. Compute monthly EMI using the formula:
  $$\text{EMI} = \frac{P \times r \times (1 + r)^n}{(1 + r)^n - 1}$$
  where $r = \frac{\text{annual\_rate}}{12 \times 100}$ and display the output rounded to 2 decimal places.
- **My Solution:**
  ```python
  loan_amount = int(input("Enter the loan Amount:"))
  annual_interest_rate = float(input("Enter the Annual Interest Rate (%):"))
  tenure = int(input("Enter the Tenure (months):"))

  monthly_interest_rate = (annual_interest_rate / 12) / 100
  EMI = (
      loan_amount
      * monthly_interest_rate
      * (1 + monthly_interest_rate)**tenure
      / ((1 + monthly_interest_rate)**tenure - 1)
  )

  print("Loan Amount:", loan_amount)
  print("Annual Interest Rate (%):", annual_interest_rate)
  print("Tenure (months):", tenure)
  print("Monthly EMI:", round(EMI, 2))
  ```
- **What I Learned & How I Solved It:**
  - Selected appropriate types for inputs: `int()` for loan principal and tenure (months), `float()` for interest percentage.
  - Implemented exponential math using Python's `**` operator with proper grouping parenthesis.
  - Used Python's built-in `round(EMI, 2)` to format currency values cleanly without long trailing decimals.

---

### 🔹 Challenge 3: Interactive Story Generator & Dual-Use Variable (`challenge3.py`)
- **Objective:** Collect 5 inputs (name, animal, number, food, city) and construct a story using an f-string. The number input must be used twice: once as text and once inside an arithmetic expression (`num * 2`).
- **My Solution:**
  ```python
  name = input("Enter Your Name:")
  animal = input("Enter an animal name:")
  num = int(input("Enter a number:"))
  food = input("Enter a food name:")
  city = input("Enter your city:")

  print(name)
  print(animal)
  print(num)
  print(food)
  print(city)

  print(f"One day in {city}, {name} met a talking {animal}. The {animal} ate {num} {food}... then asked for {num} * 2 = {num * 2} more!")
  ```
- **What I Learned & How I Solved It:**
  - Used Python f-strings (`f"..."`) to cleanly inject variables and live expressions (`{num * 2}`) into a sentence without messy string concatenation.
  - Learned that converting `num` to `int` allows it to serve both purposes: displayed as a quantity (`3`) and calculated dynamically (`3 * 2 = 6`).

