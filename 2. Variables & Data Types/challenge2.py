# challenge:
# Deriving many values from a single source variable
# Store a distance in kilometers in one variable, then convert it into several units, each held in its own variable.
# From km, compute:
# • miles       = km × 0.621
# • meters      = km × 1000
# • centimeters = km × 100000
# • feet        = km × 3280.84
# Print a formatted summary.
# Example (km = 5):
# 5 km equals:
#   Miles:       3.105
#   Meters:      5000
#   Centimeters: 500000
#   Feet:        16404.2
# Change km at the top just once and confirm every line updates automatically. Nothing else should need editing.

# Solution:
# Example with 5 km
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

# Example with 285 km
km = 285
miles = km * 0.621
meters = km * 1000
centimeters = km * 100000
feet = km * 3280.84

print("285 km equals:")
print("   Miles:      ", miles)
print("   Meters:     ", meters)
print("   Centimeters:", centimeters)
print("   Feet:       ", feet)