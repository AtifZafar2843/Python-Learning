n = int(input("enter a number:"))
for rows in range(1, n + 1):
    for space in range(rows, n):
        print(" ", end = "")
    for star in range(1, rows * 2):
        print("*", end ="")
    print()