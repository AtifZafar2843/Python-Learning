# 06. Loops

This folder covers repetition and automation in Python: using `for` loops for known sequences, `while` loops for condition-driven iterations, loop control statements, multi-level nested loops, and pattern printing.

---

## 📌 Topics Overview

### 1. `for` Loop & `range()`
- Used to iterate over a known sequence or count of items:
  ```python
  for i in range(5):        # 0, 1, 2, 3, 4
      print(i)
  ```
- **`range(start, stop, step)`**:
  - `start`: inclusive beginning value (default is 0).
  - `stop`: non-inclusive end value (stops before reaching this number).
  - `step`: increment (or decrement if negative, e.g., `range(5, 0, -1)` counts backwards).

### 2. `while` Loop
- Runs continuously as long as its condition remains `True`. Ideal when the number of iterations is not known beforehand (e.g., waiting for correct user input):
  ```python
  while guess != secret_num:
      guess = int(input("Enter guess: "))
  ```

### 3. The Infinite Loop Trap
- A `while` loop whose condition never becomes `False` will run forever, freezing the program.
- **Prevention:** Ensure the loop body modifies the variable that the condition depends on (e.g., `attempts += 1`, or updated user inputs).

### 4. `break` & `continue`
- **`break`**: Exits the loop immediately, skipping any remaining iterations.
- **`continue`**: Skips the rest of the current iteration and jumps to the next cycle.

### 5. Nested Loops & Controlling Line Breaks
- Loops placed inside other loops: the inner loop completes all its cycles for every single step of the outer loop.
- By default, `print()` ends with a newline (`\n`). Pass `end=""` to keep printing on the same line (crucial for grid and shape generation):
  ```python
  print("*", end="")  # Keeps cursor on the same line
  print()             # Moves to the next line
  ```

---

## 🎯 Challenges & Solutions

### 🔹 Challenge 1: Multiplication Table Generator (`challenge1.py`)
- **Objective:** Take a number from the user and print its complete multiplication table from 1 to 10 using a `for` loop and `range(1, 11)`.
- **My Solution:**
  ```python
  table_num = int(input("Enter a number for Table: "))

  for i in range(1, 11):
      print(f"{table_num} X {i} = {i * table_num}")
  ```
- **What I Learned & How I Solved It:**
  - Replaced 10 repetitive print statements with a single parameterized loop.
  - Used `range(1, 11)` because the stop value is non-inclusive, correctly producing multipliers 1 through 10.

---

### 🔹 Challenge 2: Number Guessing Game with Attempt Counter (`challenge2.py`)
- **Objective:** Computer generates a random secret number (0–100). The user guesses repeatedly in a `while` loop until correct, receiving "Too high" or "Too low" feedback. Track attempts and output a performance review at the end.
- **My Solution:**
  ```python
  import random

  secret_num = random.randint(0, 100)
  attemps = 0
  guess = None

  while guess != secret_num:
      guess = int(input("Guess the number between 0 to 100: "))
      attemps += 1
      if guess > secret_num:
          print("Too high!")
      elif guess < secret_num:
          print("Too low!")
      else:
          print("Congratulation! You're Correct")

  if attemps < 7:
      print(f"Excellent! You got the number in {attemps} attemps.")
  elif attemps < 10:
      print(f"Good! You got the number in {attemps} attemps.")
  else:
      print("Keep practicing!")
  ```
- **What I Learned & How I Solved It:**
  - Initialized `guess = None` and used `while guess != secret_num` to handle indeterminate loop execution.
  - Incremented an accumulator (`attemps += 1`) inside the loop to track performance.
  - Used `random.randint()` from the Python standard library.

---

### 🔹 Challenge 3: Dynamic Diamond Pattern Generator (`challenge3.py`)
- **Objective:** Take an odd number `n` and render a symmetrical diamond of stars (`*`): `n` rows for the top half (including the widest row), followed by a mirrored bottom half.
- **My Solution:**
  ```python
  n = int(input("Enter an odd number: "))

  # 1. TOP HALF (Row 1 to widest row n)
  for i in range(1, n + 1):
      for s in range(n - i):
          print(" ", end="")
      for st in range(2 * i - 1):
          print("*", end="")
      print()

  # 2. BOTTOM HALF (Reverse loop: n-1 down to 1)
  for i in range(n - 1, 0, -1):
      for s in range(n - i):
          print(" ", end="")
      for st in range(2 * i - 1):
          print("*", end="")
      print()
  ```
- **What I Learned & How I Solved It:**
  - Solved spatial geometry with math formulas:
    - Leading spaces: `n - i` spaces per row.
    - Stars per row: `2 * i - 1` (generates odd sequence: 1, 3, 5, 7...).
  - Used `range(n - 1, 0, -1)` with a negative step of `-1` to cleanly mirror the bottom pyramid without duplicating the middle row.

---

## 🌟 Star Patterns Practice (`pattern1.py` – `pattern5.py`)

A hands-on deep dive into row-column coordination, managing spaces, and manipulating inner vs. outer loop boundaries.

---

### 🔸 Pattern 1: Solid Square Grid (`pattern1.py`)
- **Concept:** Outer loop controls row count ($n$), inner loop prints stars equal to column count ($n$).
- **Code:**
  ```python
  n = int(input("enter a number:"))
  for rows in range(1, n + 1):
      for space in range(1, n + 1):
          print("*", end="")
      print()
  ```
- **Output (`n = 5`):**
  ```text
  *****
  *****
  *****
  *****
  *****
  ```
- **Key Takeaway:** Both loops run independently $n$ times, creating a fixed $n \times n$ matrix of stars.

---

### 🔸 Pattern 2: Left-Aligned Increasing Triangle (`pattern2.py`)
- **Concept:** Inner loop range is tied directly to the current row number (`range(1, rows + 1)`).
- **Code:**
  ```python
  n = int(input("enter a number:"))
  for rows in range(1, n + 1):
      for space in range(1, rows + 1):
          print("*", end="")
      print()
  ```
- **Output (`n = 5`):**
  ```text
  *
  **
  ***
  ****
  *****
  ```
- **Key Takeaway:** As `rows` increments from 1 to $n$, the inner loop executes 1 time, then 2 times, up to $n$ times.

---

### 🔸 Pattern 3: Inverted / Decreasing Triangle (`pattern3.py`)
- **Concept:** Inner loop starts from the current row value and runs up to $n + 1$ (`range(rows, n + 1)`).
- **Code:**
  ```python
  n = int(input("enter a number:"))
  for rows in range(1, n + 1):
      for space in range(rows, n + 1):
          print("*", end="")
      print()
  ```
- **Output (`n = 5`):**
  ```text
  *****
  ****
  ***
  **
  *
  ```
- **Key Takeaway:** On row 1, it prints from 1 to $n$ ($n$ stars); on row 2, from 2 to $n$ ($n - 1$ stars), gradually shrinking down to 1 star on row $n$.

---

### 🔸 Pattern 4: Right-Aligned Triangle with Spaces (`pattern4.py`)
- **Concept:** Two separate inner loops inside one outer loop: first prints decreasing spaces (`range(rows, n)`), second prints increasing stars (`range(1, rows + 1)`).
- **Code:**
  ```python
  n = int(input("enter a number:"))
  for rows in range(1, n + 1):
      for space in range(rows, n):
          print(" ", end="")
      for star in range(1, rows + 1):
          print("*", end="")
      print()
  ```
- **Output (`n = 5`):**
  ```text
      *
     **
    ***
   ****
  *****
  ```
- **Key Takeaway:** Spaces shift the stars to the right edge. On row 1, there are 4 spaces and 1 star; on row 5, there are 0 spaces and 5 stars.

---

### 🔸 Pattern 5: Centered Full Pyramid (`pattern5.py`)
- **Concept:** Combines leading spaces (`range(rows, n)`) with odd numbers of stars per row (`range(1, rows * 2)` $\rightarrow 2 \times \text{rows} - 1$ stars).
- **Code:**
  ```python
  n = int(input("enter a number:"))
  for rows in range(1, n + 1):
      for space in range(rows, n):
          print(" ", end="")
      for star in range(1, rows * 2):
          print("*", end="")
      print()
  ```
- **Output (`n = 5`):**
  ```text
      *
     ***
    *****
   *******
  *********
  ```
- **Key Takeaway:** Generates the odd sequence ($1, 3, 5, 7, 9...$) of stars centered with decreasing leading spaces, producing a symmetrical pyramid.
