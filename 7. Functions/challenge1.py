# Challenge:
# Write three functions that each RETURN an area (do not print inside them):
# • circle_area(r)        -> 3.14159 × r × r
# • rectangle_area(l, w)  -> l × w
# • triangle_area(b, h)   -> 0.5 × b × h

# Then ask the user which shape they want, collect the needed inputs, call the correct function, and print the returned result.

# Example:
# Shape (circle/rectangle/triangle): rectangle
# Length: 4
# Width: 5
# Area: 20

# Understanding return vs print here is the whole point: the functions compute and hand back a value; the main program decides how to display it.

# Solution:
def circle_area(radius: float) -> float:
    PI = 3.14159
    return PI * radius * radius


def rectangle_area(length: float, width: float) -> float:
    return length * width


def triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height



shape = input("Shape (circle/rectangle/triangle): ").strip().lower()

if shape == "circle":
        radius = float(input("Radius: "))
        print(f"Area: {circle_area(radius)}")
elif shape == "rectangle":
        length = float(input("Length: "))
        width = float(input("Width: "))
        print(f"Area: {rectangle_area(length, width)}")
elif shape == "triangle":
        base = float(input("Base: "))
        height = float(input("Height: "))
        print(f"Area: {triangle_area(base, height)}")
else:
    print("Invalid shape selected. Please choose circle, rectangle, or triangle.")