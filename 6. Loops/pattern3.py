n = int(input("enter a number:"))
for rows in range(1, n + 1):
    for space in range(rows, n + 1):
        print("*", end = "")
    print()